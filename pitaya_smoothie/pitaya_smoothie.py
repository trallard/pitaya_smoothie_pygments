from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Text,
    Number,
    Operator,
    Generic,
    Whitespace,
    Punctuation,
    Other,
    Literal,
)

#  Global colours
FOREGROUND = "#FEFEFF"
LILAC = "#B07AFC"


class PitayaSmoothie(Style):

    background_color = "#181036"
    highlight_color = "#654ea3ea"


styles = {
    # No corresponding class for the following:
    Text: FOREGROUND,  # class:  ''
    Whitespace: "#A8757B",  # class: 'w'
    Error: "#FEFEFF bg:#ff6e9c98",  # class: 'err'
    Other: "",  # class 'x'
    Comment: "#7E7AAA",  # class: 'c'
    Comment.Multiline: "",  # class: 'cm'
    Comment.Preproc: "",  # class: 'cp'
    Comment.Single: "",  # class: 'c1'
    Comment.Special: "",  # class: 'cs'
    Keyword: "#F26196",  # class: 'k' italic?
    Keyword.Constant: "#82AAFF",  # class: 'kc'
    Keyword.Declaration: "",  # class: 'kd' italic?
    Keyword.Namespace: "#C4A2F5",  # class: 'kn'
    Keyword.Pseudo: "",  # class: 'kp'
    Keyword.Reserved: "",  # class: 'kr'
    Keyword.Type: "",  # class: 'kt' italic?
    Operator: "#b07afc",  # class: 'o'
    Operator.Word: "",  # class: 'ow' - like keywords
    Punctuation: "#18c0c4",  # class: 'p'
    Name: "#FFE46B",  # class: 'n'
    Name.Attribute: LILAC,  # class: 'na'
    Name.Builtin: "#7998F2",  # class: 'nb'
    Name.Builtin.Pseudo: "#9EFFFF",  # class: 'bp'
    Name.Class: "#F26196",  # class: 'nc' italic underline?
    Name.Constant: "#7998F2",  # class: 'no'
    Name.Decorator: "#FFE46B",  # class: 'nd' underline?
    Name.Entity: "",  # class: 'ni'
    Name.Exception: LILAC,  # class: 'ne' underline?
    Name.Function: "#c6d8fa",  # class: 'nf'
    Name.Property: "#FF96B7",  # class: 'py'
    Name.Label: "",  # class: 'nl'
    Name.Namespace: "",  # class: 'nn' - to be revised
    Name.Other: "",  # class: 'nx'
    Name.Tag: "#66E9EC",  # class: 'nt' - like a keyword
    Name.Variable: LILAC,  # class: 'nv' - to be revised
    Name.Variable.Class: "",  # class: 'vc' - to be revised
    Name.Variable.Global: "",  # class: 'vg' - to be revised
    Name.Variable.Instance: "",  # class: 'vi' - to be revised
    Number: "#f3907e",  # class: 'm'
    Number.Float: "",  # class: 'mf'
    Number.Hex: "",  # class: 'mh'
    Number.Integer: "",  # class: 'mi'
    Number.Integer.Long: "",  # class: 'il'
    Number.Oct: "",  # class: 'mo'
    Literal: "#ae81ff",  # class: 'l'
    Literal.Date: "#7998F2",  # class: 'ld'
    String: "#66E9EC",  # class: 's'
    String.Backtick: "",  # class: 'sb'
    String.Char: "",  # class: 'sc'
    String.Doc: "",  # class: 'sd' - like a comment
    String.Double: "",  # class: 's2'
    String.Escape: "",  # class: 'se'
    String.Heredoc: "",  # class: 'sh'
    String.Interpol: "",  # class: 'si'
    String.Other: "",  # class: 'sx'
    String.Regex: "#5ca7e4",  # class: 'sr'
    String.Single: "",  # class: 's1'
    String.Symbol: "",  # class: 'ss'
    Generic: "",  # class: 'g'
    Generic.Deleted: "#ff6e9c",  # class: 'gd',
    Generic.Emph: "italic",  # class: 'ge'
    Generic.Error: "",  # class: 'gr'
    Generic.Heading: "",  # class: 'gh'
    Generic.Inserted: "#18c1c4a6",  # class: 'gi'
    Generic.Output: "",  # class: 'go'
    Generic.Prompt: "#A56CF5",  # class: 'gp'
    Generic.Strong: "bold",  # class: 'gs'
    Generic.Subheading: "#82b1ff",  # class: 'gu'
    Generic.Traceback: "#ff6e9c98",  # class: 'gt'
}
