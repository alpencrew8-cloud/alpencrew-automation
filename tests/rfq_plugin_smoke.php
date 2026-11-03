<?php
/* Offline WordPress contract smoke test. No WP install, network, SMTP or real POST. */
define('ABSPATH', '/tmp/');
$GLOBALS['mock_email'] = '';
$GLOBALS['mock_privacy'] = '';
function add_action($name, $callback) { /* Hook registered but not executed */ }
function add_shortcode($name, $callback) { /* Hook registered but not executed */ }
function sanitize_email($value) { return filter_var($value, FILTER_SANITIZE_EMAIL); }
function is_email($value) { return filter_var($value, FILTER_VALIDATE_EMAIL); }
function get_option($key, $default = '') { return $GLOBALS['mock_email']; }
function get_privacy_policy_url() { return $GLOBALS['mock_privacy']; }
function wp_unslash($value) { return stripslashes($value); }
function sanitize_text_field($value) { return trim(strip_tags(preg_replace('/[\r\n]+/', ' ', $value))); }
function sanitize_textarea_field($value) { return trim(strip_tags($value)); }
function sanitize_key($value) { return preg_replace('/[^a-z0-9_\-]/', '', strtolower($value)); }
function esc_url($value) { return htmlspecialchars($value, ENT_QUOTES, 'UTF-8'); }
function esc_attr($value) { return htmlspecialchars($value, ENT_QUOTES, 'UTF-8'); }
function wp_nonce_field($action, $field, $referer, $display) {
    return '<input type="hidden" name="' . $field . '" value="offline-test-nonce">';
}
function admin_url($path) { return 'https://alpencrew.com/wp-admin/' . $path; }
$GLOBALS['mock_is_product'] = false;
function is_singular($type) { return 'product' === $type && $GLOBALS['mock_is_product']; }
function get_queried_object_id() { return 123; }
function absint($value) { return abs((int) $value); }
function get_post_type($id) { return 'product'; }
function get_post_status($id) { return (int) $id === 123 ? 'publish' : 'draft'; }
function get_the_title($id) { return 'Lederhosen Men Green'; }
function get_permalink($id) { return 'https://alpencrew.com/product/lederhosen-men-short-green/'; }

require dirname(__DIR__) . '/plugins/alpencrew-b2b-rfq/alpencrew-b2b-rfq.php';

function must($truth, $message) {
    if (!$truth) { fwrite(STDERR, "FAIL: $message\n"); exit(1); }
}

must(!acrfq_ready(), 'Form should fail closed if settings are missing');
$GLOBALS['mock_email'] = 'invalid-not-an-email';
$GLOBALS['mock_privacy'] = 'https://alpencrew.com/privacy-policy/';
must(!acrfq_ready(), 'Form should reject invalid recipient');
$GLOBALS['mock_email'] = 'rfq@example.test';
must(acrfq_ready(), 'Form should accept valid owner-configured recipient and privacy policy');
must(acrfq_field(array('company' => "<b>Buyer\nCompany</b>"), 'company', 120) === 'Buyer Company',
     'User input sanitized');
must(acrfq_field(array('quantity' => array('100')), 'quantity') === '',
     'Nested array rejected');
$form = acrfq_quote_form();
foreach (array('company', 'contact_name', 'email', 'country', 'product',
               'quantity', 'sizes', 'materials', 'customization', 'delivery',
               'message', 'consent') as $field) {
    must(strpos($form, 'name="acrfq[' . $field . ']"') !== false,
         'Missing quote field: ' . $field);
}
must(strpos($form, 'alpencrew_bulk_quote_nonce') !== false, 'Missing CSRF nonce');
must(strpos($form, 'alpencrew_bulk_quote_submit') !== false, 'Missing POST handler action');
must(strpos($form, 'https://alpencrew.com/privacy-policy/') !== false, 'Missing policy link');
$GLOBALS['mock_is_product'] = true;
$product_form = acrfq_quote_form();
must(strpos($product_form, 'value="Lederhosen Men Green — https://alpencrew.com/product/lederhosen-men-short-green/"') !== false,
     'Product page should prefill only a validated live product');
$GLOBALS['mock_is_product'] = false;
$_GET['product_id'] = '999';
must(acrfq_current_product_context() === '', 'Unpublished product must not be prefilled');
$_GET['product_id'] = '123';
must(strpos(acrfq_current_product_context(), 'Lederhosen Men Green') !== false,
     'Published public WooCommerce product ID must be accepted');
unset($_GET['product_id']);
$GLOBALS['mock_privacy'] = '';
must(strpos(acrfq_quote_form(), '<form') === false, 'Should not render a form without privacy policy');
echo "SUCCESS: RFQ plugin offline security/schema tests passed. No WordPress writes or emails.\n";
