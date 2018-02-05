import pandas as pd


class List:

    @staticmethod
    def sort_this_list(rows, sort_column):

        if not rows:
            return rows, None

        df = pd.DataFrame(rows)
        df.drop_duplicates([sort_column], keep='first', inplace=True)
        df = df.sort_values(sort_column)
        df = df.reset_index(drop=True)
        return df.to_dict(orient='records'), df

    @staticmethod
    def list_to_dict(the_list, key_field):
        the_dict = {}
        for ele in the_list:
            key=ele[key_field]
            the_dict[key] = ele

        return the_dict

    @staticmethod
    def list_to_dict_of_list(the_list, key_field):
        the_dict = {}
        for ele in the_list:
            key=ele[key_field]
            if key in the_dict:
                vals = the_dict[key]
            else:
                vals=[]
            vals.append(ele)
            the_dict[key] = vals

        return the_dict

