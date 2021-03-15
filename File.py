from csv import reader

class File:
    def __init__(self):
        pass

    @staticmethod
    def read_str(fname_p) -> list:
        mlist = []

        try:
            i = 0
            with open(fname_p, 'r') as read_obj:
                csv_reader = reader(read_obj)
                i = 0
                for r in csv_reader:
                    if i > 0:
                        mlist.append(r)
                    i += 1
        except (IOError, OSError) as err:
            print(err)
            return []
        finally:
            if read_obj is not None:
                read_obj.close()
        return mlist

    @staticmethod
    def read_snp(fname_p) -> list:
        read_obj = None
        mlist = []

        try:
            i = 0
            with open(fname_p, 'r') as read_obj:
                csv_reader = reader(read_obj)
                i = 0
                for r in csv_reader:
                    if i > 0:
                        mlist.append(r)
                    i += 1
        except (IOError, OSError) as err:
            print(err)
            return []
        finally:
            if read_obj is not None:
                read_obj.close()
        return mlist
