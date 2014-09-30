c = get_config()
c.NbConvertApp.notebooks = ['*.ipynb']
c.NbConvertApp.export_format = 'slides'
#c.NbConvertApp.postprocessor_class = 'serve'
c.Exporter.template_file = 'slides.tpl'
