import sublime, sublime_plugin

class IndentDepthCommand(sublime_plugin.TextCommand):
  def run(self, edit, **args):
    self.change_indent_depth(args['depth'])

  def change_indent_depth(self, depth):
    self.view.run_command('unexpand_tabs', {'set_translate_tabs': True})
    self.view.settings().set('tab_size', depth)
    self.view.run_command('expand_tabs', {'set_translate_tabs': True})
