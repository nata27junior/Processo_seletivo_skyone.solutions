#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:40:26 2019

@author: natanael
"""


def read_txt_file():
	with open('input1.txt', 'r') as f:
		data = f.readlines()
	
	a = []

	for line in data:
		words = line.split()
		a.append(int(words[0]))

	return(a)




def alloc_users(num_clients, servers):
    _num_clients = num_clients
    _servers = servers
    while _num_clients > 0:
        server_info = get_free_server()
        if server_info[0]==0:
            i=0
        else:
            i = server_info[0]
            
        free_space = server_info[1]
        
        if _num_clients < free_space:
            _servers[i] = _num_clients
        else:
            _servers[i] = _servers[i] + free_space
        
        _num_clients = _num_clients - free_space
        _servers = [e for e in _servers if e != 0]
    return _servers


def get_free_server():

	for each in servers:	
		if each < u_max:

			free_space = u_max - each
			return((servers.index(each), free_space))
			break
		
		else:
			servers.append(0)

def calc(n, aux, t_task):

	if n == 0:
		a = aux[0]
	else:
		for each in aux:
			for i in range (len(max(aux)) - len(each)):
				each.append(0)
		
		first  = aux[-2:][0]
		second = aux[-2:][1]

		a = [x - y for x, y in zip(second, first)]

	return tuple(((n + 1) + t_task, a))




if __name__ == "__main__":
    import sys
    sys.stdout = open('saida.txt', 'w')
    print('-*'*10)
    incoming_clients_list = read_txt_file()
    servers 	 = [0]
    t_task = 5
    u_max = 10
    cost = []
    items_to_remove = []
    control_list, aux = [], []
    len_incoming_clients = len(incoming_clients_list)
    for n in range(len_incoming_clients + t_task):
        if n < t_task:
            servers = alloc_users(incoming_clients_list[n], servers)
            control_list.append(tuple(servers))		
            [aux.append(list(item)) for item in control_list]
            x = calc(n, aux, t_task)
            items_to_remove.append(x)
            cost.append(len(servers))
            tab=('\t')*1 
            print(f'{n + 1}{tab}{servers}')
            
        
        elif n >= t_task and n < len_incoming_clients:
            servers_allocation_before = control_list[-1]
            users_ratio_to_remove = items_to_remove[n - t_task][-1]
            a = [x - y for x, y in zip(servers_allocation_before, users_ratio_to_remove)]
            servers = alloc_users(incoming_clients_list[n], a)
            x = calc(n, aux, t_task)
            items_to_remove.append(x)
            cost.append(len(servers))
            tab=('\t')*1 
            print(f'{n + 1}{tab}{servers}')
            
        else:
            if servers[0] == 0:
                break	
            print(n + 1, servers)
            a = items_to_remove[(n - t_task - 1)][1]
            cost.append(len(servers))
            if sum(a) == 0:
                servers[0] = servers[0]
            else:
                servers[0] = servers[0] - 1
    
    
    print('-*'*10)
    print('='*10)
    print(f'  $: {str(sum(cost))}')		
    print('='*10)