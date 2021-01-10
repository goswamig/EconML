
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

"""Double Machine Learning. The method uses machine learning methods to identify the
part of the observed outcome and treatment that is not predictable by the controls X, W
(aka residual outcome and residual treatment).
Then estimates a CATE model by regressing the residual outcome on the residual treatment
in a manner that accounts for heterogeneity in the regression coefficient, with respect
to X.

References
----------

\\ V. Chernozhukov, D. Chetverikov, M. Demirer, E. Duflo, C. Hansen, and a. W. Newey.
    Double Machine Learning for Treatment and Causal Parameters.
    https://arxiv.org/abs/1608.00060, 2016.

\\ X. Nie and S. Wager.
    Quasi-Oracle Estimation of Heterogeneous Treatment Effects.
    arXiv preprint arXiv:1712.04912, 2017. URL http://arxiv.org/abs/1712.04912.

\\ V. Chernozhukov, M. Goldman, V. Semenova, and M. Taddy.
    Orthogonal Machine Learning for Demand Estimation: High Dimensional Causal Inference in Dynamic Panels.
    https://arxiv.org/abs/1712.09988, December 2017.

\\ V. Chernozhukov, D. Nekipelov, V. Semenova, and V. Syrgkanis.
    Two-Stage Estimation with a High-Dimensional Second Stage.
    https://arxiv.org/abs/1806.04823, 2018.

\\ Dylan Foster, Vasilis Syrgkanis (2019).
    Orthogonal Statistical Learning.
    ACM Conference on Learning Theory. https://arxiv.org/abs/1901.09036

"""

from .dml import (DML, LinearDML, SparseLinearDML,
                  KernelDML, NonParamDML, ForestDML)
from .causal_forest import CausalForestDML

__all__ = ["DML",
           "LinearDML",
           "SparseLinearDML",
           "KernelDML",
           "NonParamDML",
           "ForestDML",
           "CausalForestDML", ]