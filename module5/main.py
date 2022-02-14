from module5.Publisher import Publisher

if __name__ == "__main__":
    pub_type = Publisher.get_publication_type()
    pub_text = Publisher.get_publication_text()
    spec_info = Publisher.get_specific_info(pub_type)
    pub = Publisher.pub_builder(pub_type, pub_text, spec_info)
    Publisher.writer(pub)
