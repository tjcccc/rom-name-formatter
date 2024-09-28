from models.tag_value import TagValue

def make_tag_values_by_tags(tags):
    tag_values = []
    for index, tag in enumerate(tags):
        tag_value = TagValue(index, tag, '')
        tag_values.append(tag_value)
    return tag_values


def get_tag_value(tag: str, tag_values: list):
    for tag_value in tag_values:
        if tag_value.tag == tag:
            return tag_value
    return None


def get_tags(tag_values):
    tags = []
    for tag_value in tag_values:
        if tag_value.tag == '':
            continue
        tags.append(tag_value.tag)
    return tags
