import unittest
from scripts.seo_pilot_manifest import make_manifest, URL


class HomepageManifestTests(unittest.TestCase):
    def sample(self):
        return {
            "url": URL,
            "http_status": 200,
            "meta_noindex": False,
            "canonicals": [URL],
            "title": "Alpen Crew",
            "h1": [],
            "meta_descriptions": [],
            "og_titles": [],
            "og_descriptions": [],
        }

    def test_generates_explicit_non_live_changes(self):
        proposal = make_manifest(self.sample())
        self.assertFalse(proposal["wordpress_write_executed"])
        self.assertFalse(proposal["production_deployment_authorized"])
        self.assertEqual(len(proposal["changes"]), 5)
        self.assertIn("OWNER APPROVAL", proposal["status"])
        self.assertEqual(len(proposal["before_public_metadata_sha256"]), 64)

    def test_rejects_bad_canonical(self):
        page = self.sample()
        page["canonicals"] = ["https://other.example/"]
        with self.assertRaises(ValueError):
            make_manifest(page)

    def test_rejects_noindex(self):
        page = self.sample()
        page["meta_noindex"] = True
        with self.assertRaises(ValueError):
            make_manifest(page)

    def test_rejects_failed_fetch(self):
        page = self.sample()
        page["http_status"] = 404
        with self.assertRaises(ValueError):
            make_manifest(page)


if __name__ == "__main__":
    unittest.main()
