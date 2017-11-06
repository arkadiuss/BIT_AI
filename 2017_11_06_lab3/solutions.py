import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def _hypotheses(W, X):
    result = X.dot(W)
    return sigmoid(result)


def cost(W, X, Y, reg_param=0.1, eps=0.01):
    hypotheses = _hypotheses(W, X)
    result = Y * np.log(hypotheses + eps) + (1 - Y) * np.log(1 - hypotheses + eps)
    result = result.mean()
    result *= -1
    # print(result)
    return result  # + reg_param * np.sum(W ** 2)


def gradient_step(W, X, Y, reg_param=0.1, learning_rate=0.01):
    H = _hypotheses(W, X)

    errors = H - Y
    # print(errors)
    epsilons = (X.T.dot(errors)) / len(errors)
    return W - epsilons * learning_rate


def mean_normalization(feature_matrix):
    means = feature_matrix.mean(axis=0)
    mins = feature_matrix.min(axis=0)
    maxs = feature_matrix.max(axis=0)
    ranges = maxs - mins
    # we alter ranges and means vector so that x_0 remains unaffected
    ranges[0] = 1
    means[0] = 0
    return (feature_matrix - means) / ranges


def accuracy(actual_predictions, model_predictions):
    equals = (actual_predictions == model_predictions).astype(int)
    return equals.sum() / equals.size


def precision(actual_predictions, model_predictions):
    equals = actual_predictions == model_predictions
    eq = equals.astype(int)
    tp = actual_predictions * eq
    neq = (equals == False).astype(int)
    fp = neq * model_predictions
    return tp.sum() / (tp.sum() + fp.sum())


def recall(actual_predictions, model_predictions):
    equals = actual_predictions == model_predictions
    eq = equals.astype(int)
    tp = actual_predictions * eq
    neq = (equals == False).astype(int)
    fn = neq * (model_predictions == 0).astype(int)
    return tp.sum() / (tp.sum() + fn.sum())


def f_score(actual_predictions, model_predictions):
    p = precision(actual_predictions, model_predictions)
    r = recall(actual_predictions, model_predictions)
    return (2 * p * r) / (p + r)


tpr = recall


def fpr(actual_predictions, model_predictions):
    equals = actual_predictions == model_predictions
    eq = equals.astype(int)
    tn = (actual_predictions == 0).astype(int) * eq
    neq = (equals == False).astype(int)
    fp = neq * model_predictions
    return fp.sum() / (fp.sum() + tn.sum())