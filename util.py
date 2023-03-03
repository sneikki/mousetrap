def safe_head(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None
