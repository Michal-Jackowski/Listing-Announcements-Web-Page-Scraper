from xlsxwriter.utility import xl_col_to_name as index_to_col

MIN_MIN_FORMAT_VALUE = -500
MAX_MAX_FORMAT_VALUE = 500

def conditional_color_column(
        worksheet, df, column_name, min_format_value=None, pivot_value=0, max_format_value=None):
    """
    Do a 3 color conditional format on the column.

    The default behavior for the min and max values is to take the min and max values of each column, unless said value
    is greater than or less than the pivot value respectively at which point the values MIN_MIN_FORMAT_VALUE and
    MAX_MAX_FORMAT_VALUE are used. Also, if the min and max vales are less than or greater than respectively of
    MIN_MIN_FORMAT_VALUE and MAX_MAX_FORMAT_VALUE then the latter will be used

    :param worksheet: The worksheet on which to do the conditional formatting
    :param df: The DataFrame that was used to create the worksheet
    :param column_name: The column to format
    :param min_format_value: The value below which all cells will have the same red color
    :param pivot_value: The pivot point, values less than this number will gradient to red, values greater will gradient to green
    :param max_format_value: The value above which all cells will have the same green color
    :return: Nothing
    """
    column = df[column_name]
    min_value = min(column)
    max_value = max(column)

    last_column = len(df.index)+1
    column_index = df.columns.get_loc(column_name)
    excel_column = index_to_col(column_index)
    column_to_format = f'{excel_column}2:{excel_column}{last_column}'

    if min_format_value is None:
        min_format_value = max(min_value, MIN_MIN_FORMAT_VALUE)\
            if min_value < pivot_value else MIN_MIN_FORMAT_VALUE

    if max_format_value is None:
        max_format_value = min(max_value, MAX_MAX_FORMAT_VALUE)\
            if max_value > pivot_value else MAX_MAX_FORMAT_VALUE

    color_format = {
        'type': '3_color_scale',
        'min_type': 'num',
        'min_value': min_format_value,
        'mid_type': 'num',
        'mid_value': pivot_value,
        'max_type': 'num',
        'max_value': max_format_value
    }
    worksheet.conditional_format(column_to_format, color_format)