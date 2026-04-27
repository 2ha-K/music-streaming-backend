def rows_to_dict(rows):
    return [dict(row) for row in rows]


def row_to_dict(row):
    return dict(row) if row else None