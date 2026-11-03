<?php
/**
 * Plugin Name: Alpen Crew B2B Quote Form (Staging Candidate)
 * Description: Opt-in wholesale quotation shortcode; not active unless owner installs, configures and places [alpencrew_bulk_quote].
 * Version: 0.1.0
 * Requires PHP: 7.4
 * License: GPL-2.0-or-later
 */
defined('ABSPATH') || exit;

const ACRFQ_RECIPIENT_OPTION = 'acrfq_recipient';

add_action('admin_init', static function () {
    register_setting('acrfq_settings', ACRFQ_RECIPIENT_OPTION, array(
        'type' => 'string',
        'sanitize_callback' => static function ($value) {
            $email = sanitize_email(is_string($value) ? $value : '');
            return is_email($email) ? $email : '';
        },
        'default' => '',
    ));
});

add_action('admin_menu', static function () {
    add_options_page('Alpen Crew RFQ', 'Alpen Crew RFQ', 'manage_options', 'alpencrew-rfq', 'acrfq_settings_page');
});

function acrfq_settings_page() {
    if (!current_user_can('manage_options')) {
        wp_die(esc_html__('Insufficient permission.', 'alpencrew-b2b-rfq'));
    }
    ?>
    <div class="wrap">
      <h1><?php echo esc_html__('Alpen Crew — wholesale quote recipient', 'alpencrew-b2b-rfq'); ?></h1>
      <p>Set a verified company-controlled email. This plugin does not certify mail delivery; test with a real internal submission before publishing the form.</p>
      <form method="post" action="options.php">
        <?php settings_fields('acrfq_settings'); ?>
        <label for="acrfq-recipient">Recipient email address</label>
        <input id="acrfq-recipient" type="email" class="regular-text" required
               name="<?php echo esc_attr(ACRFQ_RECIPIENT_OPTION); ?>"
               value="<?php echo esc_attr((string) get_option(ACRFQ_RECIPIENT_OPTION, '')); ?>" />
        <?php submit_button(); ?>
      </form>
    </div>
    <?php
}

function acrfq_ready() {
    $recipient = (string) get_option(ACRFQ_RECIPIENT_OPTION, '');
    return is_email($recipient) && get_privacy_policy_url();
}

function acrfq_field($source, $key, $limit = 200, $multiline = false) {
    if (!isset($source[$key]) || !is_string($source[$key])) {
        return '';
    }
    $raw = wp_unslash($source[$key]);
    $value = $multiline ? sanitize_textarea_field($raw) : sanitize_text_field($raw);
    return function_exists('mb_substr') ? mb_substr($value, 0, $limit) : substr($value, 0, $limit);
}

function acrfq_current_product_context() {
    $id = 0;
    if (function_exists('is_singular') && is_singular('product')) {
        $id = (int) get_queried_object_id();
    } elseif (isset($_GET['product_id']) && is_string($_GET['product_id'])) {
        // A product ID is public catalog metadata, never a buyer identifier.
        $id = absint(wp_unslash($_GET['product_id']));
    }
    if ($id > 0 && 'product' === get_post_type($id) && 'publish' === get_post_status($id)) {
        return sanitize_text_field(get_the_title($id) . ' — ' . get_permalink($id));
    }
    return '';
}

function acrfq_quote_form() {
    if (!acrfq_ready()) {
        return '<p class="alpencrew-rfq-unavailable">The business quotation form is not yet available. Please use the contact page.</p>';
    }
    $policy = esc_url(get_privacy_policy_url());
    $status = isset($_GET['acrfq_status']) && is_string($_GET['acrfq_status'])
        ? sanitize_key(wp_unslash($_GET['acrfq_status'])) : '';
    ob_start();
    if ('sent' === $status) {
        echo '<p role="status">Your business enquiry was received for processing. Please retain a copy of your submission.</p>';
    } elseif ('failed' === $status) {
        echo '<p role="alert">The enquiry could not be sent. Please try again or use our contact page.</p>';
    } elseif ('invalid' === $status) {
        echo '<p role="alert">Please check the required quotation fields and submit again.</p>';
    }
    ?>
    <form class="alpencrew-rfq" method="post" action="<?php echo esc_url(admin_url('admin-post.php')); ?>">
      <input type="hidden" name="action" value="alpencrew_bulk_quote_submit">
      <?php echo wp_nonce_field('alpencrew_bulk_quote_submit', 'alpencrew_bulk_quote_nonce', true, false); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
      <div class="alpencrew-rfq-honey" style="position:absolute;left:-9999px" aria-hidden="true">
        <label>Leave this field blank <input type="text" name="acrfq_company_fax" value="" tabindex="-1" autocomplete="off"></label>
      </div>
      <p><label for="acrfq-company">Company name *</label>
        <input id="acrfq-company" name="acrfq[company]" type="text" maxlength="120" required autocomplete="organization"></p>
      <p><label for="acrfq-buyer">Buyer/contact name *</label>
        <input id="acrfq-buyer" name="acrfq[contact_name]" type="text" maxlength="120" required autocomplete="name"></p>
      <p><label for="acrfq-email">Work email *</label>
        <input id="acrfq-email" name="acrfq[email]" type="email" maxlength="190" required autocomplete="email"></p>
      <p><label for="acrfq-website">Business website</label>
        <input id="acrfq-website" name="acrfq[business_url]" type="url" maxlength="200" placeholder="https://"></p>
      <p><label for="acrfq-country">Business country *</label>
        <input id="acrfq-country" name="acrfq[country]" type="text" maxlength="90" required autocomplete="country-name"></p>
      <p><label for="acrfq-product">Product/category or existing Alpen Crew product URL *</label>
        <input id="acrfq-product" name="acrfq[product]" type="text" maxlength="200" value="<?php echo esc_attr(acrfq_current_product_context()); ?>" required></p>
      <p><label for="acrfq-quantity">Requested quantity (pieces) *</label>
        <input id="acrfq-quantity" name="acrfq[quantity]" type="number" min="1" max="1000000" step="1" required inputmode="numeric"></p>
      <p><label for="acrfq-sizes">Size breakdown</label>
        <textarea id="acrfq-sizes" name="acrfq[sizes]" maxlength="1000"></textarea></p>
      <p><label for="acrfq-material">Materials/fabric requirements</label>
        <textarea id="acrfq-material" name="acrfq[materials]" maxlength="1000"></textarea></p>
      <p><label for="acrfq-custom">Branding/customization requests</label>
        <textarea id="acrfq-custom" name="acrfq[customization]" maxlength="1000"></textarea></p>
      <p><label for="acrfq-delivery">Target delivery date and country</label>
        <input id="acrfq-delivery" name="acrfq[delivery]" type="text" maxlength="180"></p>
      <p><label for="acrfq-details">Additional procurement details</label>
        <textarea id="acrfq-details" name="acrfq[message]" maxlength="2000"></textarea></p>
      <p><label for="acrfq-consent"><input id="acrfq-consent" name="acrfq[consent]" type="checkbox" value="yes" required>
        I agree that Alpen Crew may use these details to respond to my quotation enquiry.
        See the <a href="<?php echo $policy; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>">privacy policy</a>.</label></p>
      <button type="submit">Send Bulk Quotation Request</button>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('alpencrew_bulk_quote', 'acrfq_quote_form');

function acrfq_redirect($status) {
    $ref = wp_get_referer();
    $path = $ref ? wp_parse_url($ref, PHP_URL_PATH) : '/contact-us/';
    if (!is_string($path) || !$path || '/' !== substr($path, 0, 1) || '//' === substr($path, 0, 2)) {
        $path = '/contact-us/';
    }
    $safe_destination = add_query_arg('acrfq_status', $status, home_url($path));
    wp_safe_redirect($safe_destination, 303);
    exit;
}

function acrfq_submit() {
    if ('POST' !== (isset($_SERVER['REQUEST_METHOD']) ? strtoupper((string) $_SERVER['REQUEST_METHOD']) : '')) {
        wp_die('Invalid request.', '', array('response' => 405));
    }
    if (!isset($_POST['alpencrew_bulk_quote_nonce']) ||
        !is_string($_POST['alpencrew_bulk_quote_nonce']) ||
        !wp_verify_nonce(sanitize_text_field(wp_unslash($_POST['alpencrew_bulk_quote_nonce'])), 'alpencrew_bulk_quote_submit')) {
        wp_die('Invalid request.', '', array('response' => 403));
    }
    if (!acrfq_ready()) {
        wp_die('Quote form not configured.', '', array('response' => 503));
    }
    // Honeypot must remain empty. No responses or data are stored for spam submissions.
    if (!empty($_POST['acrfq_company_fax'])) {
        acrfq_redirect('sent');
    }
    if (!isset($_POST['acrfq']) || !is_array($_POST['acrfq'])) {
        acrfq_redirect('invalid');
    }
    $data = $_POST['acrfq'];
    $company = acrfq_field($data, 'company', 120);
    $buyer = acrfq_field($data, 'contact_name', 120);
    $email = sanitize_email(acrfq_field($data, 'email', 190));
    $country = acrfq_field($data, 'country', 90);
    $product = acrfq_field($data, 'product', 200);
    $quantity = acrfq_field($data, 'quantity', 8);
    $consent = acrfq_field($data, 'consent', 8);
    if (!$company || !$buyer || !is_email($email) || !$country || !$product ||
        !ctype_digit($quantity) || (int) $quantity < 1 || (int) $quantity > 1000000 ||
        'yes' !== $consent) {
        acrfq_redirect('invalid');
    }
    $business_url = acrfq_field($data, 'business_url', 200);
    if ($business_url && (!in_array(wp_parse_url($business_url, PHP_URL_SCHEME), array('http', 'https'), true) ||
        !wp_parse_url($business_url, PHP_URL_HOST))) {
        acrfq_redirect('invalid');
    }

    // Rate limit on a salted hash; never store the raw visitor IP address.
    $client_ip = isset($_SERVER['REMOTE_ADDR']) ? (string) $_SERVER['REMOTE_ADDR'] : 'unknown';
    $rate_key = 'acrfq_' . substr(hash_hmac('sha256', $client_ip, wp_salt('auth')), 0, 40);
    $count = (int) get_transient($rate_key);
    if ($count >= 6) {
        wp_die('Too many requests. Please try again later.', '', array('response' => 429));
    }
    set_transient($rate_key, $count + 1, 10 * MINUTE_IN_SECONDS);

    $fields = array(
        'Company' => $company,
        'Buyer name' => $buyer,
        'Work email' => $email,
        'Business website' => $business_url,
        'Country' => $country,
        'Product/style' => $product,
        'Pieces requested' => $quantity,
        'Size breakdown' => acrfq_field($data, 'sizes', 1000, true),
        'Material requirements' => acrfq_field($data, 'materials', 1000, true),
        'Customization' => acrfq_field($data, 'customization', 1000, true),
        'Delivery' => acrfq_field($data, 'delivery', 180),
        'Other details' => acrfq_field($data, 'message', 2000, true),
        'Privacy consent' => 'yes',
    );
    $lines = array();
    foreach ($fields as $label => $value) {
        $lines[] = $label . ': ' . $value;
    }
    $recipient = (string) get_option(ACRFQ_RECIPIENT_OPTION, '');
    $sent = wp_mail(
        $recipient,
        '[Alpen Crew B2B RFQ] New wholesale enquiry',
        implode("\n\n", $lines),
        array('Content-Type: text/plain; charset=UTF-8', 'Reply-To: ' . $email)
    );
    // wp_mail true means accepted by configured mailer, NOT confirmed inbox delivery.
    acrfq_redirect($sent ? 'sent' : 'failed');
}
add_action('admin_post_nopriv_alpencrew_bulk_quote_submit', 'acrfq_submit');
add_action('admin_post_alpencrew_bulk_quote_submit', 'acrfq_submit');
