from ff_data import ff_data


def main():
    feature_flags = ff_data()
    feature_flags.extract_audit_data()


if __name__ == "__main__":
    main()