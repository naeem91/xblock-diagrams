"""
Xblock for generating diagrams from text. The text is simple markdown-like script language.
This is a simple wrapper around mermaid (https://github.com/knsv/mermaid)
"""

import textwrap
import pkg_resources

from xblock.core import XBlock
from xblock.fields import String, Scope
from xblock.fragment import Fragment

from xblockutils.studio_editable import StudioEditableXBlockMixin

from utils import _


class DiagramsXBlock(StudioEditableXBlockMixin, XBlock):
    """
    Xblock for generating diagrams from text
    """
    display_name = String(
        display_name=_("Display Name"),
        help=_("This name appears in the horizontal navigation at the top of the page."),
        scope=Scope.settings,
        default=_("Diagrams")
    )
    markup = String(
        display_name='Markup',
        help=_("Markup for generating diagrams. "
               "See http://knsv.github.io/mermaid/#/examples for syntax."),
        multiline_editor=True,
        resettable_editor=False,
        scope=Scope.content,
        default=textwrap.dedent("""\
        <h1>Flowchart</h1>
        <div class="mermaid">
            graph LR
                A[Square Rect] -- Link text --> B((Circle))
                A --> C(Round Rect)
                B --> D{Rhombus}
                C --> D
        </div>
        <h1>Sequence diagram</h1>
        <div class="mermaid">
            sequenceDiagram
                participant Alice
                participant Bob
                Alice->>John: Hello John, how are you?
                loop Healthcheck
                    John->>John: Fight against hypochondria
                end
                Note right of John: Rational thoughts <br/>prevail!
                John-->>Alice: Great!
                John->>Bob: How about you?
                Bob-->>John: Jolly good!
        </div>
        """))

    editable_fields = ('display_name', 'markup',)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the DiagramsXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/diagrams.html")
        frag = Fragment(html.format(markup=self.markup))
        frag.add_css(self.resource_string("static/css/diagrams.css"))
        frag.add_javascript(self.resource_string("static/js/src/diagrams.js"))

        frag.add_javascript_url(url='//unpkg.com/mermaid@8.3.1/dist/mermaid.min.js')
        frag.initialize_js('DiagramsXBlock')
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("DiagramsXBlock",
             """<diagrams/>
             """),
            ("Multiple DiagramsXBlock",
             """<vertical_demo>
                <diagrams/>
                <diagrams/>
                <diagrams/>
                </vertical_demo>
             """),
        ]
