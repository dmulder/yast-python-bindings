#include "YPythonCode.h"
#include <Python.h>

YPythonCode::YPythonCode (PyObject *pFunc, PyObject *pArgs):YCode() {
    m_kind = YCode::yeReference;
    _pFunc = pFunc;
    _pArgs = pArgs;
}

YCPValue YPythonCode::evaluate(bool cse) {
    PyObject * pReturn = NULL;
    YCPValue result = YCPVoid();

    if (!PyFunction_Check(_pFunc) || (_pArgs != NULL and !PyTuple_Check(_pArgs))) {
        return result;
    }

    if (Py_IsInitialized()) {
        pReturn = PyObject_CallObject(_pFunc, _pArgs);
        if (pReturn)
            result = pyval_to_ycp(pReturn);
    }
    return result;
}

YCode::ykind YPythonCode::kind() const {
    return m_kind;
}

std::ostream & YPythonCode::toStream (std::ostream & str) const {
    return str;
}

std::ostream & YPythonCode::toXml (std::ostream & str, int indent ) const {
    return str;
}

