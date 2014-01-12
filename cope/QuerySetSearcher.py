from django.db.models import Q

def normalize_query(query_string,
					findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
					normspace=re.compile(r'\s{2,}').sub):
	'''
	Splits the query string in invidual keywords.

	Also removes unecessary spaces and grouping quoted words together.
	returns a list of keywords
	Example:
	>>> normalize_query('  some random  words "with   quotes  " and   spaces')
	['some', 'random', 'words', 'with quotes', 'and', 'spaces']
	'''
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
	'''
	Returns a query, that is a combination of Q objects. That combination
	aims to search keywords within a model by testing the given search fields.

	Example:
	>>> query_list = get_query(query_string, ['field1', 'field2', ...])
	>>> result = ModelName.objects.filter(query_list)
	'''
	# Query to search for every search term
	query = None
	terms = normalize_query(query_string)
	for term in terms:
		# Query to search for a given term in each field
		term_query = None
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if term_query is None:
				term_query = q
			else:
				term_query = term_query | q
		if query is None:
			query = term_query
		else:
			query = query | term_query
	return query
