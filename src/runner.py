thonimport json
from extractors.linkedin_parser import parse_profile
from outputs.exporters import export_to_json, export_to_csv

def run_scraper(input_file, output_file, output_format="json"):
    try:
        with open(input_file, "r") as file:
            profiles = json.load(file)
        
        extracted_data = []
        for profile_url in profiles['urls']:
            profile_data = parse_profile(profile_url)
            extracted_data.append(profile_data)
        
        if output_format == "json":
            export_to_json(extracted_data, output_file)
        elif output_format == "csv":
            export_to_csv(extracted_data, output_file)
        else:
            raise ValueError("Unsupported output format")
        print(f"Scraping complete. Data exported to {output_file}.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    input_file = "data/inputs.sample.txt"
    output_file = "data/sample_output.json"
    run_scraper(input_file, output_file)