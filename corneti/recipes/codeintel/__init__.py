import os
import simplejson as json
import zc.recipe.egg


class CodeintelRecipe(object):

    SUPPORTED_LANGUAGES = ['PHP', 'Python', 'RHTML', 'JavaScript', 'Smarty', 'Mason', 'Node.js', 'XBL', 'Tcl', 'HTML',
        'HTML5', 'TemplateToolkit', 'XUL', 'Django', 'Perl', 'Ruby', 'Python3']

    def __init__(self, buildout, name, options):

        self.buildout, self.name, self.options = buildout, name, options

        # Read .codeintel directory from options or just dump in the buildout root
        default_target = os.path.join(self.buildout['buildout']['directory'], '.codeintel')
        target = options.get("codeintel-path", default_target)

        self.codeintel_directory = target

        if not os.path.exists(self.codeintel_directory):
            os.mkdir(self.codeintel_directory)

        self._python = self.buildout['buildout']['executable']

        # form extra paths dictionary where each key is lang and value is a list of paths
        config = {}
        for lang in self.SUPPORTED_LANGUAGES:
            lang_lower = lang.lower()
            lang_extra_paths = filter(None, map(lambda x: x.strip(),
                options.get('{0}-extra-paths'.format(lang_lower), '').split()))
            if lang_extra_paths:
                config.setdefault(lang, {})
                config[lang]['{0}ExtraPaths'.format(lang_lower)] = lang_extra_paths
            lang_path = options.get('{0}-path'.format(lang_lower), '')
            if lang_path:
                config[lang][lang_lower] = lang_path

        # update formed dict with extra-paths option
        python_extra_paths = options.get('extra-paths', '').split('\n')
        python_extra_paths = filter(lambda p: p.strip() != '', python_extra_paths)

        config.setdefault('Python', {}).setdefault('pythonExtraPaths', []).extend(python_extra_paths)

        self.config = config

        self.egg = zc.recipe.egg.Egg(self.buildout, self.name, self.options)

    def install(self):
        python_paths = (filter(None, map(lambda p: p.strip(), self.egg.working_set()[1].entries)) +
            self.config['Python']['pythonExtraPaths'])
        self.config['Python']['pythonExtraPaths'] = python_paths
        open(os.path.join(self.codeintel_directory, "config"), "w").write(json.dumps(self.config, indent=4,
            sort_keys=True))
        return ""

    def update(self):
        return self.install()
