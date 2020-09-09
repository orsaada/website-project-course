# The data for your website

data = {
    # Example of a collection
    "dogs": [
        {
            "size": 'small',
            "name": 'ask',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/orAsk.jpeg'
        },
        {
            "size": 'small',
            "name": 'coding',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20coding.jpeg'
        },
        {
            "size": 'medium',
            "name": 'ballons',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20100%20ballons.jpeg'
        },
        {
            "size": 'small',
            "name": 'boom',
            'snippet': " ",
            'imageUrl': '/shared/images/orrr/or%20boom.jpeg'
        },
        {
            "size": 'small',
            "name": 'who',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20asking%20who.jpeg'
        },
        {
            "size": 'small',
            "name": 'staring cat',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20staring%20cat.jpeg'
        },
        {
            "size": 'small',
            "name": 'dollars',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20100%20dollar.jpeg'
        },
        {
            "size": 'small',
            "name": 'ballons laugh',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20ballons%20lagth.jpeg'
        },
        {
            "size": 'small',
            "name": 'crying',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20crying.jpeg'
        },
        {
            "size": 'small',
            "name": 'dancing',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20dancing.jpeg'
        },
        {
            "size": 'small',
            "name": 'popcorn',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20popcorn.jpeg'
        },
        {
            "size": 'small',
            "name": 'subscribed',
            'snippet': "",
            'imageUrl': '/shared/images/orrr/or%20unsubscribed.jpeg'
        },
    ],
    "images": [
        {"url": '/shared/images/orrr/orAsk.jpeg'},
        {"url": '/shared/images/orrr/or%20coding.jpeg'},
        {"url": '/shared/images/orrr/or%20100%20ballons.jpeg'},
        {"url": '/shared/images/orrr/or%20boom.jpeg'},
        {"url": '/shared/images/orrr/or%20asking%20who.jpeg'},
        {"url": '/shared/images/orrr/or%20staring%20cat.jpeg'},
        {"url": '/shared/images/orrr/or%20100%20dollar.jpeg'},
        {"url": '/shared/images/orrr/or%20ballons%20lagth.jpeg'},
        {"url": '/shared/images/orrr/or%20crying.jpeg'},
        {"url": '/shared/images/orrr/or%20dancing.jpeg'},
        {"url": '/shared/images/orrr/or%20popcorn.jpeg'},
        {"url": '/shared/images/orrr/or%20unsubscribed.jpeg'},
    ],
    "sizes": [
        {"name": "small", "toString": "Small"},
        {"name": "medium", "toString": "Medium"},
        {"name": "big", "toString": "Big"},
    ],
    "cities": [
        {"id": "telAviv", "toString": "Tel Aviv xoxo"},
        {"id": "2", "toString": "Haifa"}
    ],
    "days": [0, 1, 2],
    "hours": [[1, 2, 3, 4], [2, 3, 4], [3, 4]]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = list(filter(lambda element: set(params.items()).issubset(set(element.items())),
                                data[collection]))

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
