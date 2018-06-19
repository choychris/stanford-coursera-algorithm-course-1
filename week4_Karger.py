from random import choice

# line_list = [line.rstrip('\n') for line in open('./_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt')]
# # print (line_list);
# graph_dict = {}
# for row in line_list:
#   row_list = list(map(int, row.split()))
#   graph_dict[row_list[0]] = row_list[1:]
graph_dict = { 
  1: [3,4,2],
  2: [1,4,3],
  3: [1,2,4],
  4: [5,3,2,1],
  5: [4,8,6,7],
  6: [8,7,5],
  7: [5,8,6],
  8: [5,7,6]
}

def contraction(graph_dict_list):
  if len(graph_dict_list) == 2:
    return len(graph_dict_list[list(graph_dict_list.keys())[0]])

  # randomly pick two Vs
  firstV = choice(list(graph_dict_list.keys()))
  secondV = choice(graph_dict_list[firstV])
  # print ('firstV', firstV)
  # print ('secondV', secondV)
  # print (graph_dict_list[firstV])
  # connect other V to the merged 2nd V
  for each in graph_dict_list[firstV]:
    # print (each)
    if (each == secondV):
      graph_dict_list[each] = [x for x in graph_dict_list[each] if x != firstV ]
    else:
      graph_dict_list[each] = [secondV if x == firstV else x for x in graph_dict_list[each]]
  # remove 2nd V in picked list(remove the edge)
  graph_dict_list[firstV].remove(secondV)
  # concat picked list to 2nd V list (merge all the edges)
  graph_dict_list[secondV] = graph_dict_list[secondV] + graph_dict_list[firstV]
  # remove the picked list(1st V)
  del graph_dict_list[firstV]
  # remove self loop
  graph_dict_list[secondV] = [x for x in graph_dict_list[secondV] if x != secondV ]
  # recursion
  # print (graph_dict_list)
  return contraction(graph_dict_list)

def counting(graph):
  min_cut = 0
  run = 0
  for i in range (5):
    count = 0
    print(graph.copy()[1])
    count = contraction(graph.copy())
    run = run + 1
    # print (run)
    print ('count after', count)
    if(i == 0):
      min_cut = count
    elif count < min_cut:
      min_cut = count
  return min_cut

print (counting(graph_dict))
# print (contraction(graph_dict))