def init_header():
    header = \
    '\\version "2.18.2" \n\
    \paper {\n\
    #(set-paper-size "a4landscape") \n\
    print-all-headers = ##t \n\
    } \n\
    \layout{ \n\
      indent = 0\in \n\
      ragged-last = ##f \n\
      \context { \n\
        \Score \n\
      } \n\
    }\\new Voice \with { \n\
      \\remove "Note_heads_engraver" \n\
      \\consists "Completion_heads_engraver" \n\
      \\remove "Rest_engraver" \n\
      \\consists "Completion_rest_engraver" \n\
    }\n'
    return header
