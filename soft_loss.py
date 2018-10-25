import torch

def hinton_softmax(tensor, smooth):
  smooth_exp = torch.exp(tensor.float() / smooth)
  return smooth_exp / torch.sum(smooth_exp)

vals = torch.tensor([1, 10, 0, -100])
vals_sm = hinton_softmax(vals, 20)
print(vals_sm)
print(vals_sm.sum())
vals_sm = hinton_softmax(vals, 1)
print(vals_sm)
print(vals_sm.sum())
