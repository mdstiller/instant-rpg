class Entry(tornado.web.UIModule)
	def embedded_css(self):
		return ".entry {margin-bottom: lem; }"
		
	def render(self, entry, show_comments=False):
		return self.render_string(
			"module-entry.html", entry=entry, show_comments=show_comments)