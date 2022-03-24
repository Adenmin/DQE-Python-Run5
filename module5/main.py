from module5.DBConnector import DBConnector
from module5.NewsFeedStatistic import NewsFeedStatistic
from module5.Publication import PublicationMethod, PublicationType
from module5.Publisher import Publisher
from module5.RawParser import RawParser

if __name__ == "__main__":
    pub_method = Publisher.get_pub_method()

    # Get publication from input.
    if pub_method is PublicationMethod.manual:
        pub_type = Publisher.get_publication_type()
        pub_text = Publisher.get_publication_text()
        spec_info = Publisher.get_specific_info(pub_type)
        pub = Publisher.build_publication(pub_type, pub_text, spec_info)
        Publisher.write_to_newsfeed(pub)
        db_connector = DBConnector(pub_type.name)
        with db_connector.connection:
            db_connector.insert(pub)

    # Get publication from file.
    elif pub_method is PublicationMethod.fromFile:
        file_path = Publisher.get_file_path()
        rp = RawParser(file_path)
        raw_pubs = rp.parse_raw_file()
        for p in raw_pubs:
            pub = Publisher.build_publication(PublicationType.from_str(p['type']), p['text'], p['spec_info'])
            Publisher.write_to_newsfeed(pub)
            db_connector = DBConnector(p['type'])
            with db_connector.connection:
                db_connector.insert(pub)
        rp.delete_raw_file()

    # Write newsfeed statistic to csv files.
    nfs = NewsFeedStatistic('newsfeed.txt')
    nfs.write_word_statistic('statistic_words.csv')
    nfs.write_letter_statistic('statistic_letters.csv')
