from module5.Publication import PublicationMethod, PublicationType
from module5.Publisher import Publisher
from module5.RawParser import RawParser

if __name__ == "__main__":
    pub_method = Publisher.get_pub_method()
    if pub_method is PublicationMethod.manual:
        pub_type = Publisher.get_publication_type()
        pub_text = Publisher.get_publication_text()
        spec_info = Publisher.get_specific_info(pub_type)
        pub = Publisher.pub_builder(pub_type, pub_text, spec_info)
        Publisher.writer(pub)
    elif pub_method is PublicationMethod.fromFile:
        file_path = Publisher.get_file_path()
        rp = RawParser(file_path)
        pubs = rp.parse_raw_file()
        for pub in pubs:
            Publisher.writer(
                Publisher.pub_builder(PublicationType.from_str(pub['type']), pub['text'], pub['spec_info']))
        rp.delete_raw_file()
