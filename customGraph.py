import dgl
import torch
data_dict = {
    ('user', 'follows', 'topic'): (torch.tensor([1, 1]), torch.tensor([1, 2])),
    ('user', 'plays', 'game'): (torch.tensor([0, 3]), torch.tensor([3, 4])),
    ('game', 'based-on', 'topic'): (torch.tensor([3, 4]), torch.tensor([4, 5]))
}
g = dgl.heterograph(data_dict)
print(g)
# Node and Edge Features
g.nodes['user'].data['U'] = torch.ones(4, 1)
g.nodes['game'].data['G'] = torch.ones(5,1)
g.nodes['topic'].data['T'] = torch.ones(6,1)

g.edges['follows'].data['UvsT'] = torch.ones(2,1)
g.edges['plays'].data['UvsG'] = torch.ones(2,1)
g.edges['based-on'].data['GvsT'] = torch.ones(2,1)
print(g.nodes['topic'].data['T'], g.edges['based-on'].data['GvsT'])
dgl.save_graphs('graph.dgl', g)
