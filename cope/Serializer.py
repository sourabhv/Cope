from StringIO import StringIO

from django.core.serializers.json import Serializer

class JSONSerializer(Serializer):
	'''
	JSON serialize to serialize db fields and properties

	Example:
	>>> JSONSerializer().serialize(Model.objects.all(), ('field1', 'field2',))
	'''
	def serialize(self, queryset, attributes, **options):
		self.options = options
		self.stream = options.get("stream", StringIO())
		self.start_serialization()
		self.first = True

		for obj in queryset:
			self.start_object(obj)
			for field in attributes:
				self.handle_field(obj, field)
			self.end_object(obj)
			if self.first:
				self.first = False
		self.end_serialization()
		return self.getvalue()

	def handle_field(self, obj, field):
		self._current[field] = getattr(obj, field)
