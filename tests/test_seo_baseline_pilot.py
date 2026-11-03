import unittest
from scripts.seo_baseline_pilot import Metadata, valid_url

class PilotTests(unittest.TestCase):
    def test_allowlist(self):
        self.assertTrue(valid_url("https://alpencrew.com/product-category/men/"))
        for url in ("http://alpencrew.com/", "https://fakealpencrew.com/",
                    "https://alpencrew.com.evil.test/",
                    "https://user:pass@alpencrew.com/"):
            self.assertFalse(valid_url(url))

    def test_missing_metadata_and_h1(self):
        parser = Metadata()
        parser.feed("<html><head><title>Example</title></head><body>"
                    "<img src='/decoration.png' alt=''></body></html>")
        result = parser.to_public_record()
        self.assertEqual(result["title"], "Example")
        self.assertEqual(result["h1_count"], 0)
        self.assertEqual(result["images_empty_alt_including_decorative"], 1)
        self.assertIn("missing description", result["flags"])
        self.assertIn("missing canonical", result["flags"])
        self.assertIn("missing H1", result["flags"])

    def test_metadata_and_noindex(self):
        parser = Metadata()
        parser.feed('<html><head><title>Men</title>'
                    '<meta name="description" content="Traditional garments">'
                    '<meta property="og:title" content="Men catalog">'
                    '<meta name="robots" content="noindex,follow">'
                    '<link rel="canonical" href="https://alpencrew.com/cart/">'
                    '</head><body><h1>Bulk <span>enquiries</span></h1></body></html>')
        result = parser.to_public_record()
        self.assertTrue(result["meta_noindex"])
        self.assertEqual(result["h1"], ["Bulk enquiries"])
        self.assertEqual(result["canonicals"], ["https://alpencrew.com/cart/"])
        self.assertNotIn("missing canonical", result["flags"])
        self.assertNotIn("missing OG title", result["flags"])

if __name__ == "__main__":
    unittest.main()
