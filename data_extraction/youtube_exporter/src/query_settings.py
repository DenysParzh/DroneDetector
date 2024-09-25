class QuerySettings:
    def __init__(self, query, max_count,
                 region_code=None, exclude=None,
                 published_after: dict = None, published_before: dict = None):

        if isinstance(query, str):
            query = [query]

        if not exclude and isinstance(exclude, str):
            exclude = [exclude]

        self.query = query
        self.max_count = max_count
        self.exclude = exclude
        self.published_after = self._parse_date(published_after) if published_after else None
        self.published_before = self._parse_date(published_before) if published_after else None
        self.region_code = "UA" if not region_code else region_code
        self.part = "id,snippet"

    def get_query_string(self):
        query_string = ""

        for q in self.query:
            query_string += f"|{q}"

        if self.exclude:
            for e in self.exclude:
                query_string += f" -{e}"

        return query_string[1:]

    @staticmethod
    def _parse_date(date: dict) -> str:
        year = date["year"]
        month = date["month"]
        day = date["day"]
        return f"{year}-{month}-{day}T00:00:00Z"
