import unittest
from scripts.b2b_enquiry_audit import classify_fields


class LeadFormSchemaTests(unittest.TestCase):
    def test_wholesale_form_coverage(self):
        forms = [{"field_descriptors": [
            {"field_name": "company-name"},
            {"field_name": "work_email"},
            {"field_name": "country"},
            {"field_name": "product"},
            {"field_name": "order-quantity"},
            {"field_name": "size-breakdown"},
            {"field_name": "fabric"},
            {"field_name": "expected-delivery-date"},
        ]}]
        result = classify_fields(forms)
        self.assertTrue(all(result[k] for k in (
            "business_or_company", "work_email", "country", "product",
            "quantity", "sizes", "material", "timeline")))
        self.assertFalse(result["phone"])

    def test_empty_or_retail_only_form(self):
        result = classify_fields([{"field_descriptors": [
            {"field_name": "your-name"},
            {"field_name": "email"},
            {"field_name": "message"},
        ]}])
        self.assertTrue(result["work_email"])
        self.assertTrue(result["message"])
        self.assertFalse(result["business_or_company"])
        self.assertFalse(result["quantity"])

    def test_no_forms(self):
        self.assertTrue(all(not value for value in classify_fields([]).values()))


if __name__ == "__main__":
    unittest.main()
