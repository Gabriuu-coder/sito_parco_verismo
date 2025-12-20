# Guard per evitare che il package venga importato come modulo top-level 'tests'
# (ciò causa problemi con unittest discovery nel contesto di questo progetto).
if __name__ != "parco_verismo.tests":
    raise ImportError(
        "Importare il package come 'parco_verismo.tests' (non come modulo top-level 'tests')"
    )
