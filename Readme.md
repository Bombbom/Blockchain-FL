# Blockchain for Federated Learning 

----
## Reference 


----
## Implement

```
sudo apt install python3
sudo apt install python3-vevn
python3 -m vevn env
source env/bin/activate
pip install -r package.txt
##Som error
pip install -U tensorflow 
```


### Creating datasets for n clients

- mnist dataset:
  - 
- data/federated_data_extractor.py
  - get_mnist(): func to get mnist images dataset from tensorflow site
  - save_data(dataset,name="mnist.d"): Func to save mnist data in binary mode(its good to use binary mode)
  - load_data(name="mnist.d"): Func to load mnist data in binary mode(for reading also binary mode is important)
  - get_dataset_details(dataset): Func to display information on data
  - split_dataset(dataset,split_count): Function to split dataset to federated data slices as per specified count so as to try federated learning

```python
if __name__ == '__main__':
    save_data(get_mnist())
    dataset = load_data()
    get_dataset_details(dataset)
    for n,d in enumerate(split_dataset(dataset,2)):
        save_data(d,"federated_data_"+str(n)+".d")
        dk = load_data("federated_data_"+str(n)+".d")
        get_dataset_details(dk)
        print()
```
- Load mnist dataset from server
- save -> mnist.d
- load dataset -> split dataset (federated_data_0.d and federated_data_1.d) -> show information of dataset
- output
```
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11490434/11490434 [==============================] - 1s 0us/step
train_images (60000, 784)
train_labels (60000, 10)
test_images (10000, 784)
test_labels (10000, 10)
test_images (10000, 784)
test_labels (10000, 10)
train_images (30000, 784)
train_labels (30000, 10)

test_images (10000, 784)
test_labels (10000, 10)
train_images (30000, 784)
train_labels (30000, 10)
```

### Start federated learning on n clients 

```
python3 miner.py -g 1 -l 2
```

- blockchain.py
  - compute_global_model(base,updates,lrate): Function to compute the global model based on the client updates received per round
  - find_len(text,strk):Function to find the specified string in the text and return its starting position as well as length/last_index
  - class Update
  - class Block
  - class Blockchain

- federatedlearner.py
  - 
- miner.py
  - 

- run

```python
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    parser.add_argument('-i', '--host', default='127.0.0.1', help='IP address of this miner')
    parser.add_argument('-g', '--genesis', default=0, type=int, help='instantiate genesis block')
    parser.add_argument('-l', '--ulimit', default=10, type=int, help='number of updates stored in one block')
    parser.add_argument('-ma', '--maddress', help='other miner IP:port')
    args = parser.parse_args()
    address = "{host}:{port}".format(host=args.host,port=args.port)
    status['address'] = address
    if args.genesis==0 and args.maddress==None:
        raise ValueError("Must set genesis=1 or specify maddress")
    delete_prev_blocks()
    if args.genesis==1:
        model = make_base()
        print("base model accuracy:",model['accuracy'])
        status['blockchain'] = Blockchain(address,model,True,args.ulimit)
    else:
        status['blockchain'] = Blockchain(address)
        status['blockchain'].register_node(args.maddress)
        requests.post('http://{node}/nodes/register'.format(node=args.maddress),
            json={'nodes': [address]})
        status['blockchain'].resolve_conflicts(STOP_EVENT)
    app.run(host=args.host,port=args.port)
```


### Start client

### Create_csv


## Reult 

```
{"chain":[{"accuracy":"0.1132","hash":"2f6939a94518bc4fb1b29d09629457f1779f6b6482babdb74f1144932c24405a","index":1,"miner":"127.0.0.1:5000","model_hash":"416af99a0233f728633a4b68548b9722c155e6ae232102c3078eaa739bd60d8e","previous_hash":1,"proof":71385075,"time_limit":1800,"timestamp":1669996122.669962,"update_limit":2},{"accuracy":"0.6928","hash":"07657fe5e75b975be4dd44cac4154e5449318269dbac05492ba5d76aabace8bf","index":2,"miner":"127.0.0.1:5000","model_hash":"8dd118058198c0dd3cd8a71a32ed5b5cc7474d1337a2039e2a56ca9d5d5d5c45","previous_hash":"c9f8ec2b520a07f473929e45e24165725c7de09eee29f8aeb13a4e7b57749be2","proof":25387736,"time_limit":1800,"timestamp":1669996357.0475159,"update_limit":2}],"length":2}
```

```
{"last_model_index":2,"status":"receiving"}
```


```
127.0.0.1 - - [02/Dec/2022 22:48:47] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [02/Dec/2022 22:48:47] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [02/Dec/2022 22:48:54] "GET /block HTTP/1.1" 405 -
127.0.0.1 - - [02/Dec/2022 22:49:25] "GET //nodes/resolve HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:49:33] "GET /nodes/resolve HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:49:43] "GET /nodes/model HTTP/1.1" 404 -
127.0.0.1 - - [02/Dec/2022 22:50:14] "GET /model HTTP/1.1" 405 -
127.0.0.1 - - [02/Dec/2022 22:50:21] "GET /chain HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:50:39] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:50:49] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:50:49] "GET /chain HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:50:49] "POST /model HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:50:52] "POST /transactions/new HTTP/1.1" 201 -
127.0.0.1 - - [02/Dec/2022 22:50:56] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:50:56] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:51:00] "GET /chain HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:51:05] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:51:32] "GET //nodes/resolve HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:51:39] "GET /nodes/resolve HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:17] "GET /stopmining HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:22] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:33] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:33] "GET /chain HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:33] "POST /model HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:36] "POST /transactions/new HTTP/1.1" 201 -
mining 24686000
mining 24687000
mining 24688000
mining 24689000
mining 24690000
mining 24691000
mining 24692000
mining 24693000
mining 24694000
mining 24695000
mining 24696000
mining 24697000
mining 24698000
mining 24699000
mining 24700000
mining 24701000
mining 24702000
mining 24703000
mining 24704000
mining 24705000
mining 24706000
mining 24707000
mining 24708000
mining 24709000
mining 24710000
mining 24711000
mining 24712000
mining 24713000
mining 24714000
mining 24715000
mining 24716000
mining 24717000
mining 24718000
mining 24719000
mining 24720000
mining 24721000
mining 24722000
mining 24723000
mining 24724000
mining 24725000
mining 24726000
mining 24727000
mining 24728000
mining 24729000
mining 24730000
mining 24731000
mining 24732000
mining 24733000
mining 24734000
mining 24735000
mining 24736000
mining 24737000
mining 24738000
mining 24739000
mining 24740000
mining 24741000
mining 24742000
mining 24743000
mining 24744000
mining 24745000
mining 24746000
mining 24747000
mining 24748000
mining 24749000
mining 24750000
mining 24751000
mining 24752000
mining 24753000
mining 24754000
mining 24755000
mining 24756000
mining 24757000
mining 24758000
mining 24759000
mining 24760000
mining 24761000
mining 24762000
mining 24763000
mining 24764000
mining 24765000
mining 24766000
mining 24767000
mining 24768000
mining 24769000
mining 24770000
mining 24771000
mining 24772000
mining 24773000
mining 24774000
mining 24775000
mining 24776000
mining 24777000
mining 24778000
mining 24779000
mining 24780000
mining 24781000
mining 24782000
mining 24783000
mining 24784000
mining 24785000
mining 24786000
mining 24787000
mining 24788000
mining 24789000
mining 24790000
mining 24791000
mining 24792000
mining 24793000
mining 24794000
mining 24795000
mining 24796000
mining 24797000
mining 24798000
mining 24799000
mining 24800000
mining 24801000
mining 24802000
mining 24803000
mining 24804000
mining 24805000
mining 24806000
mining 24807000
mining 24808000
mining 24809000
mining 24810000
mining 24811000
mining 24812000
mining 24813000
mining 24814000
mining 24815000
mining 24816000
mining 24817000
mining 24818000
mining 24819000
mining 24820000
mining 24821000
mining 24822000
mining 24823000
mining 24824000
mining 24825000
mining 24826000
mining 24827000
mining 24828000
mining 24829000
mining 24830000
mining 24831000
mining 24832000
mining 24833000
mining 24834000
mining 24835000
mining 24836000
mining 24837000
mining 24838000
mining 24839000
mining 24840000
mining 24841000
mining 24842000
mining 24843000
mining 24844000
mining 24845000
mining 24846000
mining 24847000
mining 24848000
mining 24849000
mining 24850000
mining 24851000
mining 24852000
mining 24853000
mining 24854000
mining 24855000
mining 24856000
mining 24857000
mining 24858000
mining 24859000
mining 24860000
mining 24861000
mining 24862000
mining 24863000
mining 24864000
mining 24865000
mining 24866000
mining 24867000
mining 24868000
mining 24869000
mining 24870000
mining 24871000
mining 24872000
mining 24873000
mining 24874000
mining 24875000
mining 24876000
mining 24877000
mining 24878000
mining 24879000
mining 24880000
mining 24881000
mining 24882000
mining 24883000
mining 24884000
mining 24885000
mining 24886000
mining 24887000
mining 24888000
mining 24889000
mining 24890000
mining 24891000
mining 24892000
mining 24893000
mining 24894000
mining 24895000
mining 24896000
mining 24897000
mining 24898000
mining 24899000
mining 24900000
mining 24901000
mining 24902000
mining 24903000
mining 24904000
mining 24905000
mining 24906000
mining 24907000
mining 24908000
mining 24909000
mining 24910000
mining 24911000
mining 24912000
mining 24913000
mining 24914000
mining 24915000
mining 24916000
mining 24917000
mining 24918000
mining 24919000
mining 24920000
mining 24921000
mining 24922000
mining 24923000
mining 24924000
mining 24925000
mining 24926000
mining 24927000
mining 24928000
mining 24929000
mining 24930000
mining 24931000
mining 24932000
mining 24933000
mining 24934000
mining 24935000
mining 24936000
mining 24937000
mining 24938000
mining 24939000
mining 24940000
mining 24941000
mining 24942000
mining 24943000
mining 24944000
mining 24945000
mining 24946000
mining 24947000
mining 24948000
mining 24949000
mining 24950000
mining 24951000
mining 24952000
mining 24953000
mining 24954000
mining 24955000
mining 24956000
mining 24957000
mining 24958000
mining 24959000
mining 24960000
mining 24961000
mining 24962000
mining 24963000
mining 24964000
mining 24965000
mining 24966000
mining 24967000
mining 24968000
mining 24969000
mining 24970000
mining 24971000
mining 24972000
mining 24973000
mining 24974000
mining 24975000
mining 24976000
mining 24977000
mining 24978000
mining 24979000
mining 24980000
mining 24981000
mining 24982000
mining 24983000
mining 24984000
mining 24985000
mining 24986000
mining 24987000
mining 24988000
mining 24989000
mining 24990000
mining 24991000
mining 24992000
mining 24993000
mining 24994000
mining 24995000
mining 24996000
mining 24997000
mining 24998000
mining 24999000
mining 25000000
mining 25001000
mining 25002000
mining 25003000
mining 25004000
mining 25005000
mining 25006000
mining 25007000
mining 25008000
mining 25009000
mining 25010000
mining 25011000
mining 25012000
mining 25013000
mining 25014000
mining 25015000
mining 25016000
mining 25017000
mining 25018000
mining 25019000
mining 25020000
mining 25021000
mining 25022000
mining 25023000
mining 25024000
mining 25025000
mining 25026000
mining 25027000
mining 25028000
mining 25029000
mining 25030000
mining 25031000
mining 25032000
mining 25033000
mining 25034000
mining 25035000
mining 25036000
mining 25037000
mining 25038000
mining 25039000
mining 25040000
mining 25041000
mining 25042000
mining 25043000
mining 25044000
mining 25045000
mining 25046000
mining 25047000
mining 25048000
mining 25049000
mining 25050000
mining 25051000
mining 25052000
mining 25053000
mining 25054000
mining 25055000
mining 25056000
mining 25057000
mining 25058000
mining 25059000
mining 25060000
mining 25061000
mining 25062000
mining 25063000
mining 25064000
mining 25065000
mining 25066000
mining 25067000
mining 25068000
mining 25069000
mining 25070000
mining 25071000
mining 25072000
mining 25073000
mining 25074000
mining 25075000
mining 25076000
mining 25077000
mining 25078000
mining 25079000
mining 25080000
mining 25081000
mining 25082000
mining 25083000
mining 25084000
mining 25085000
mining 25086000
mining 25087000
mining 25088000
mining 25089000
mining 25090000
mining 25091000
mining 25092000
mining 25093000
mining 25094000
mining 25095000
mining 25096000
mining 25097000
mining 25098000
mining 25099000
mining 25100000
mining 25101000
mining 25102000
mining 25103000
mining 25104000
mining 25105000
mining 25106000
mining 25107000
mining 25108000
mining 25109000
mining 25110000
mining 25111000
mining 25112000
mining 25113000
mining 25114000
mining 25115000
mining 25116000
mining 25117000
mining 25118000
mining 25119000
mining 25120000
mining 25121000
mining 25122000
mining 25123000
mining 25124000
mining 25125000
mining 25126000
mining 25127000
mining 25128000
mining 25129000
mining 25130000
mining 25131000
mining 25132000
mining 25133000
mining 25134000
mining 25135000
mining 25136000
mining 25137000
mining 25138000
mining 25139000
mining 25140000
mining 25141000
mining 25142000
mining 25143000
mining 25144000
mining 25145000
mining 25146000
mining 25147000
mining 25148000
mining 25149000
mining 25150000
mining 25151000
mining 25152000
mining 25153000
mining 25154000
mining 25155000
mining 25156000
mining 25157000
mining 25158000
mining 25159000
mining 25160000
mining 25161000
mining 25162000
mining 25163000
mining 25164000
mining 25165000
mining 25166000
mining 25167000
mining 25168000
mining 25169000
mining 25170000
mining 25171000
mining 25172000
mining 25173000
mining 25174000
mining 25175000
mining 25176000
mining 25177000
mining 25178000
mining 25179000
mining 25180000
mining 25181000
mining 25182000
mining 25183000
mining 25184000
mining 25185000
mining 25186000
mining 25187000
mining 25188000
mining 25189000
mining 25190000
mining 25191000
mining 25192000
mining 25193000
mining 25194000
mining 25195000
mining 25196000
mining 25197000
mining 25198000
mining 25199000
mining 25200000
mining 25201000
mining 25202000
mining 25203000
mining 25204000
mining 25205000
mining 25206000
mining 25207000
mining 25208000
mining 25209000
mining 25210000
mining 25211000
mining 25212000
mining 25213000
mining 25214000
mining 25215000
mining 25216000
mining 25217000
mining 25218000
mining 25219000
mining 25220000
mining 25221000
mining 25222000
mining 25223000
mining 25224000
mining 25225000
mining 25226000
mining 25227000
mining 25228000
mining 25229000
mining 25230000
mining 25231000
mining 25232000
mining 25233000
mining 25234000
mining 25235000
mining 25236000
mining 25237000
mining 25238000
mining 25239000
mining 25240000
mining 25241000
mining 25242000
mining 25243000
mining 25244000
mining 25245000
mining 25246000
mining 25247000
mining 25248000
mining 25249000
mining 25250000
mining 25251000
mining 25252000
mining 25253000
mining 25254000
mining 25255000
mining 25256000
mining 25257000
mining 25258000
mining 25259000
mining 25260000
mining 25261000
mining 25262000
mining 25263000
mining 25264000
mining 25265000
mining 25266000
mining 25267000
mining 25268000
mining 25269000
mining 25270000
mining 25271000
mining 25272000
mining 25273000
mining 25274000
mining 25275000
mining 25276000
mining 25277000
mining 25278000
mining 25279000
mining 25280000
mining 25281000
mining 25282000
mining 25283000
mining 25284000
mining 25285000
mining 25286000
mining 25287000
mining 25288000
mining 25289000
mining 25290000
mining 25291000
mining 25292000
mining 25293000
mining 25294000
mining 25295000
mining 25296000
mining 25297000
mining 25298000
mining 25299000
mining 25300000
mining 25301000
mining 25302000
mining 25303000
mining 25304000
mining 25305000
mining 25306000
mining 25307000
mining 25308000
mining 25309000
mining 25310000
mining 25311000
mining 25312000
mining 25313000
mining 25314000
mining 25315000
mining 25316000
mining 25317000
mining 25318000
mining 25319000
mining 25320000
mining 25321000
mining 25322000
mining 25323000
mining 25324000
mining 25325000
mining 25326000
mining 25327000
mining 25328000
mining 25329000
mining 25330000
mining 25331000
mining 25332000
mining 25333000
mining 25334000
mining 25335000
mining 25336000
mining 25337000
mining 25338000
mining 25339000
mining 25340000
mining 25341000
mining 25342000
mining 25343000
mining 25344000
mining 25345000
mining 25346000
mining 25347000
mining 25348000
mining 25349000
mining 25350000
mining 25351000
mining 25352000
mining 25353000
mining 25354000
mining 25355000
mining 25356000
mining 25357000
mining 25358000
mining 25359000
mining 25360000
mining 25361000
mining 25362000
mining 25363000
mining 25364000
mining 25365000
mining 25366000
mining 25367000
mining 25368000
mining 25369000
mining 25370000
mining 25371000
mining 25372000
mining 25373000
mining 25374000
mining 25375000
mining 25376000
mining 25377000
mining 25378000
mining 25379000
mining 25380000
mining 25381000
mining 25382000
mining 25383000
mining 25384000
mining 25385000
mining 25386000
mining 25387000
Done
127.0.0.1 - - [02/Dec/2022 22:52:47] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:52:53] "GET /chain HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:54:14] "GET /nodes/resolve HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:55:11] "GET /chain HTTP/1.1" 200 -
127.0.0.1 - - [02/Dec/2022 22:58:55] "GET /status HTTP/1.1" 200 -
```

```
$ python3 client.py -d data/federated_data_1.d -e 1
2022-12-02 22:52:32.688181: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-02 22:52:32.789124: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-12-02 22:52:32.789141: I tensorflow/compiler/xla/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2022-12-02 22:52:33.355592: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.355642: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.355650: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
--------------
b64fa2bc06a549d2aca6b7475d0c0c19  Dataset info:
test_images (10000, 784)
test_labels (10000, 10)
train_images (30000, 784)
train_labels (30000, 10)
--------------
b6 device_id
--------------
Accuracy global model 0.1132
2022-12-02 22:52:33.964014: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-02 22:52:33.964279: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964341: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcublas.so.11'; dlerror: libcublas.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964381: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcublasLt.so.11'; dlerror: libcublasLt.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964419: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcufft.so.10'; dlerror: libcufft.so.10: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964471: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcurand.so.10'; dlerror: libcurand.so.10: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964524: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcusolver.so.11'; dlerror: libcusolver.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964582: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcusparse.so.11'; dlerror: libcusparse.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964621: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudnn.so.8'; dlerror: libcudnn.so.8: cannot open shared object file: No such file or directory
2022-12-02 22:52:33.964643: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1934] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2022-12-02 22:52:33.964997: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:From /home/bombbom/Documents/Malware_Project/env/lib/python3.8/site-packages/tensorflow/python/compat/v2_compat.py:107: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
2022-12-02 22:52:33.986715: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:357] MLIR V1 optimization pass is not enabled
2022-12-02 22:52:34.121645: W tensorflow/c/c_api.cc:291] Operation '{name:'bo/Assign' id:26 op device:{requested: '', assigned: ''} def:{{{node bo/Assign}} = Assign[T=DT_FLOAT, _class=["loc:@bo"], _has_manual_control_dependencies=true, use_locking=true, validate_shape=true](bo, bo/initial_value)}}' was changed by setting attribute after it was run by a session. This mutation will have no effect, and will trigger an error in the future. Either don't modify nodes after running them or create a new session.
Step 1, Minibatch Loss= 10261.0527, Training Accuracy= 0.278
Optimization Finished!
Step 2, Minibatch Loss= 13458.5771, Training Accuracy= 0.449
Optimization Finished!
Step 3, Minibatch Loss= 20745.8555, Training Accuracy= 0.306
Optimization Finished!
Step 4, Minibatch Loss= 26798.0527, Training Accuracy= 0.286
Optimization Finished!
Step 5, Minibatch Loss= 12647.6348, Training Accuracy= 0.483
Optimization Finished!
Step 6, Minibatch Loss= 7513.1348, Training Accuracy= 0.525
Optimization Finished!
Step 7, Minibatch Loss= 3758.3386, Training Accuracy= 0.597
Optimization Finished!
Step 8, Minibatch Loss= 2620.1843, Training Accuracy= 0.695
Optimization Finished!
Step 9, Minibatch Loss= 3880.3452, Training Accuracy= 0.591
Optimization Finished!
Step 10, Minibatch Loss= 3935.5422, Training Accuracy= 0.595
Optimization Finished!
Accuracy local update---------b6--------------: 0.5954
```

```
$ python3 client.py -d data/federated_data_0.d -e 1
2022-12-02 22:50:48.101540: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-12-02 22:50:48.206540: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-12-02 22:50:48.206558: I tensorflow/compiler/xla/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2022-12-02 22:50:48.787406: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory
2022-12-02 22:50:48.787455: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory
2022-12-02 22:50:48.787462: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
--------------
be3ebf73893b4654866e2614ee215472  Dataset info:
test_images (10000, 784)
test_labels (10000, 10)
train_images (30000, 784)
train_labels (30000, 10)
--------------
be device_id
--------------
Accuracy global model 0.1132
2022-12-02 22:50:49.411112: I tensorflow/compiler/xla/stream_executor/cuda/cuda_gpu_executor.cc:981] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2022-12-02 22:50:49.412435: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.412694: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcublas.so.11'; dlerror: libcublas.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.412909: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcublasLt.so.11'; dlerror: libcublasLt.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.413185: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcufft.so.10'; dlerror: libcufft.so.10: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.413441: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcurand.so.10'; dlerror: libcurand.so.10: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.413675: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcusolver.so.11'; dlerror: libcusolver.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.413943: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcusparse.so.11'; dlerror: libcusparse.so.11: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.414145: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudnn.so.8'; dlerror: libcudnn.so.8: cannot open shared object file: No such file or directory
2022-12-02 22:50:49.414185: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1934] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2022-12-02 22:50:49.415060: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
WARNING:tensorflow:From /home/bombbom/Documents/Malware_Project/env/lib/python3.8/site-packages/tensorflow/python/compat/v2_compat.py:107: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
2022-12-02 22:50:49.454773: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:357] MLIR V1 optimization pass is not enabled
2022-12-02 22:50:49.565282: W tensorflow/c/c_api.cc:291] Operation '{name:'bo/Assign' id:26 op device:{requested: '', assigned: ''} def:{{{node bo/Assign}} = Assign[T=DT_FLOAT, _class=["loc:@bo"], _has_manual_control_dependencies=true, use_locking=true, validate_shape=true](bo, bo/initial_value)}}' was changed by setting attribute after it was run by a session. This mutation will have no effect, and will trigger an error in the future. Either don't modify nodes after running them or create a new session.
Step 1, Minibatch Loss= 10238.5771, Training Accuracy= 0.283
Optimization Finished!
Step 2, Minibatch Loss= 13512.6914, Training Accuracy= 0.461
Optimization Finished!
Step 3, Minibatch Loss= 21061.5039, Training Accuracy= 0.303
Optimization Finished!
Step 4, Minibatch Loss= 27532.3398, Training Accuracy= 0.291
Optimization Finished!
Step 5, Minibatch Loss= 14535.8613, Training Accuracy= 0.515
Optimization Finished!
Step 6, Minibatch Loss= 10262.3740, Training Accuracy= 0.495
Optimization Finished!
Step 7, Minibatch Loss= 4072.9558, Training Accuracy= 0.630
Optimization Finished!
Step 8, Minibatch Loss= 3047.4507, Training Accuracy= 0.679
Optimization Finished!
Step 9, Minibatch Loss= 4406.0195, Training Accuracy= 0.576
Optimization Finished!
Step 10, Minibatch Loss= 4794.7925, Training Accuracy= 0.551
Optimization Finished!
Accuracy local update---------be--------------: 0.5612
```

```
$ python3 create_csv.py
['/home/bombbom/Documents/Malware_Project/clients/devicebe_model_v0.block', '/home/bombbom/Documents/Malware_Project/clients/deviceb6_model_v0.block']
```

```
b1 ->>> [-1.73002914e-01 -6.02670252e-01  1.89083576e-01  1.15450025e+00
 -2.28175912e-02 -1.39990819e+00  9.53265607e-01  1.01843536e+00
 -6.02870584e-01 -5.64323425e-01  5.94743431e-01  1.67570263e-01
  7.69012570e-01 -2.12416363e+00  2.34975362e+00  4.49481338e-01
  6.07170701e-01  1.55750179e+00  5.50727487e-01 -8.64857495e-01
  1.19984090e-01 -1.23893864e-01 -3.39556724e-01 -3.62898946e-01
  5.03739834e-01 -7.88769647e-02 -9.54060614e-01 -2.04394341e+00
 -8.97927463e-01  3.78648430e-01 -3.56436223e-01 -1.31740701e+00
  8.69810998e-01  1.56272873e-01 -1.22509766e+00  6.90287173e-01
  8.62398684e-01 -5.34500659e-01 -2.31612206e-01  1.71324599e+00
 -1.75191367e+00  1.10042930e+00 -7.09236979e-01 -2.45507762e-01
 -7.82822192e-01 -1.14887893e+00  6.89376816e-02  4.34283167e-01
 -1.31838381e+00 -2.16537535e-01  7.20930934e-01 -1.16937685e+00
 -3.61544162e-01 -4.68937457e-02  2.47450941e-03 -1.33102345e+00
 -2.11055622e-01 -7.61669636e-01 -4.72562611e-02 -6.04841888e-01
  4.61196363e-01 -5.09395182e-01  5.20002484e-01 -9.28222165e-02
  4.84390795e-01 -9.71628726e-02 -5.13690054e-01 -1.04713058e+00
 -5.18625557e-01  1.96581078e+00 -1.93641171e-01 -2.37392008e-01
 -5.02872050e-01  2.66727948e+00  1.82829988e+00  9.72364604e-01
 -4.04975891e-01  1.37052226e+00 -4.47596908e-01 -1.45746851e+00
 -1.54554927e+00 -6.18014812e-01  4.77868706e-01  7.35415101e-01
  2.49432102e-01 -3.06412756e-01 -1.40900278e+00 -1.82434350e-01
 -1.38409257e+00  1.16975904e+00  1.65073037e-01 -1.26437354e+00
 -1.13893640e+00 -2.80617863e-01 -4.23885360e-02 -4.75206494e-01
 -4.12870944e-01 -9.78658974e-01  1.14020813e+00 -1.57737032e-01
  2.19301417e-01  8.66198719e-01 -2.28315264e-01 -5.14877319e-01
  9.29010630e-01  3.91056150e-01 -1.99000371e+00  2.55297542e-01
 -3.15952271e-01  1.31526554e+00  3.71686459e-01  3.81253481e-01
  1.90975595e+00 -8.03463012e-02 -1.38111854e+00 -1.11531758e+00
 -1.93903768e+00 -5.15838146e-01 -1.44721293e+00  1.17723417e+00
  2.10065432e-02 -3.30605507e-01  1.89920619e-01  9.12373960e-02
  1.76132210e-02 -9.58365649e-02  2.44019318e+00  1.34539545e+00
  1.08675741e-01  3.22790980e-01  8.99256691e-02  1.95739090e+00
 -4.84163165e-01 -6.92428827e-01  1.36336340e-02 -5.09956241e-01
  7.26688266e-01  6.75425947e-01  5.11976600e-01  9.30467427e-01
  1.06726205e+00  7.48234451e-01 -5.60137451e-01  4.21605110e-01
  1.00969183e+00  7.79994845e-01  1.32540369e+00  2.28836268e-01
 -1.65817106e+00  6.99255407e-01 -8.74679387e-01  1.23391783e+00
  2.40721881e-01 -2.52502680e-01  9.69517291e-01  3.63653675e-02
  1.21473685e-01  4.82821435e-01 -4.58314478e-01 -2.73282230e-01
  1.13597691e+00 -4.64045405e-02 -7.99783707e-01 -1.22899926e+00
  4.37470257e-01  6.24797285e-01 -2.78103054e-01 -1.86995542e+00
 -1.00800538e+00  5.64636707e-01  7.74556339e-01  1.20286152e-01
  5.21940589e-01  4.61868733e-01 -7.93870211e-01  1.33556449e+00
  2.41161108e-01  1.04184508e+00 -8.35832596e-01  1.29090154e+00
  2.38373414e-01 -3.78067136e-01 -2.08459663e+00  1.53164792e+00
 -8.25673521e-01  1.03499711e+00 -1.39394629e+00 -9.06448603e-01
 -1.18045747e+00  1.10087764e+00  1.23417556e+00 -4.84177709e-01
 -7.64684737e-01  2.68023968e-01 -1.37694383e+00  1.14308798e+00
 -8.36288452e-01  1.94425058e+00  1.44427466e+00 -2.05357615e-02
  1.09885097e+00  4.72886443e-01 -9.41061318e-01  1.05676398e-01
  4.22650427e-01  1.43315256e-01  3.07976753e-01 -4.15855229e-01
 -2.87186772e-01  6.01089954e-01 -1.92674309e-01 -1.39755785e+00
 -1.44144833e-01  7.93358624e-01  1.77009165e+00  2.08448321e-01
 -1.12505758e+00 -2.09015310e-01 -1.40121472e+00 -1.42944002e+00
 -5.39420307e-01  9.96914387e-01 -7.90108085e-01 -1.40571630e+00
 -1.36681509e+00  3.58937114e-01 -9.58005011e-01 -9.39788163e-01
 -3.60898823e-01 -1.46582460e+00  4.71436590e-01  1.81556270e-01
  8.73298228e-01 -1.17341578e+00 -1.85280752e+00  4.19951439e-01
  8.91250372e-01  4.65219289e-01  1.51307869e+00  1.54700831e-01
  7.93666542e-01 -1.18607235e+00  1.37859118e+00  7.65129745e-01
  8.55622947e-01 -1.56307864e+00  1.20795405e+00 -3.26093554e-01
  1.18362129e+00  3.68103504e-01 -2.53942060e+00 -1.05928974e-02
 -1.85248971e-01 -5.68623424e-01 -4.68920141e-01  1.51219463e+00]

b2 ->>> [-1.1145091  -0.16674066  0.16258085 -0.5183258   2.2800531  -1.0150315
 -0.22995737  0.23253472  1.4441402  -0.573431   -0.48414847  1.4792936
 -0.17259747 -1.3875076   0.21357264  1.0225055   0.09187599 -2.0456939
  0.95946926 -0.24021314  0.93321085  0.29345083 -1.9624543   0.34230462
  0.32247216 -0.14326183 -2.6726382   0.67350185  1.3841726   0.950137
  0.71884733  0.40755993 -0.48392212  0.56093377  0.13052477  1.2271467
 -0.5796257   0.45353514  0.41637754 -0.93226147 -0.39653358  0.13649623
  0.5909992   0.58066094 -1.032547    0.06402919 -0.62834924 -2.0259683
  1.9707935   0.46555093 -1.4001118   0.2422555   0.7497304   1.2995998
 -0.21088593  2.3726363  -1.1150633   1.4384313   1.7130487  -1.7828909
 -0.45410314 -0.30195823  0.34369904 -0.6929553   0.06606536 -2.4842296
  0.30476767  1.18846    -1.057051    0.14049298 -0.26614696 -1.3602813
  0.476217    0.6301353  -1.0742227  -0.89033604 -0.16667266  0.48641974
  0.37997553  1.7525914  -1.3597902  -0.53274924  1.2216457  -0.8267647
 -0.87147623 -0.03859551  0.59228224  0.7939967  -0.27261946  0.07003243
 -0.3061643  -0.42282376 -0.51061064 -0.41029677  1.4996792   1.7721221
 -0.66921234 -0.7503495  -0.17612992 -1.4013544   2.5618827   1.9222732
  1.380436    0.53124017 -1.062943   -0.45419496  0.31966716 -0.25030312
  0.57352114  0.05366936  0.15246758  0.5897989  -1.7696856  -0.4354662
 -0.25414485 -0.5061371   0.18931736  2.3096373  -1.3172188   0.20896253
  0.7475854  -0.910207    0.96370035  0.3227369   0.9612089  -1.1226499
 -0.08987183 -0.25953773  0.5294944  -1.5892663  -0.17920385 -1.5888488
 -0.7525761  -0.08252116 -0.77090615 -1.8980821  -0.62000734 -0.02870904
 -0.90163714 -0.65600014  1.1488885   0.8513564  -0.17703448  0.22123161
 -1.885813   -0.24812326 -0.0413783  -0.8008289  -0.04209262 -0.34854755
  0.28290713 -0.45808992  0.4897164   0.96035874 -0.12264232  1.2104175
  2.5357533  -0.6777184   1.2275455  -0.45474112 -1.0158675  -1.0925019
 -0.76867276 -0.54998106  0.8179554   0.817425    2.588599   -1.4376068
 -0.6616568   2.4994779   0.35438886 -0.6974359   1.8890877   0.3104851
 -0.17608906 -1.2977328  -0.66368115 -0.25772032  1.5208929  -1.2695332
  1.2260531  -1.5126867   0.96993846  1.0545876  -0.41184032  0.92408025
 -0.11078069 -0.37009534  0.07369282 -0.00435059 -0.45675823 -0.05612012
  0.77539897  0.23019934  0.44429487 -2.0718644   0.73558885 -1.0817964
 -0.8803779  -0.16406296  0.17238115  0.02599274 -0.9238688   2.2234054
 -0.12274016  0.6886022   0.58520806 -0.742345   -0.63434637 -0.28054765
  0.0170704  -0.0866731  -0.33478692  0.9042875   0.43361738  0.3594012
 -0.06040132  0.13342467 -0.13417438 -0.8881199  -0.07649439  0.13000323
  0.31297672 -0.87490547 -0.4877295   1.6966779  -1.3520993  -1.2291714
 -0.67381495 -0.22644226 -0.9283478   0.02653472  0.01722548 -0.09057339
  0.4572785   1.2918557   2.038116   -2.0423186  -0.46176675  0.06430651
 -1.7110832   0.01082074 -0.17666888  1.5945392  -0.5626681  -1.7598712
  1.3024465  -0.74466306 -0.14144962  0.33727196  1.2706689   0.5922582
  0.7488166  -1.3666152   0.93260044 -0.70713836]

bo ->>> [ 0.73413575  0.2825237  -1.921938   -0.72647053 -0.4293656   1.3317422
 -0.33458528 -1.2790968   0.9590205  -0.01026011]

size ->>> 0

w1 ->>> [[-0.3695798   0.4027207  -0.09957074 ... -0.44750357  0.41442442
  -0.01979898]
 [-0.7247589  -0.7045253   0.22509618 ...  0.52442896 -0.5247873
  -0.98940104]
 [-0.15699483  0.04995154 -0.4624561  ...  1.8899322   0.44933283
  -0.15276943]
 ...
 [ 0.37865078  0.95644957  0.0925568  ...  1.3892828  -0.22093152
   0.36195508]
 [-1.7802182   0.85878956  0.8031334  ...  0.93309885  0.8838574
  -1.1030841 ]
 [-0.9537363  -0.28754503 -0.69443303 ...  0.3023356   1.0707577
  -0.1995611 ]]

w2 ->>> [[-0.01140308 -1.106364    0.5150119  ... -0.84844536  0.54547626
   0.4211408 ]
 [-0.1930666  -0.61665964  0.44378555 ...  0.6557537  -1.1119016
   0.23900075]
 [-0.2179929   0.10615227  0.7352323  ... -1.0057838   2.1128201
   1.3173051 ]
 ...
 [ 0.8026881  -1.0648754  -0.7805089  ...  1.6199636  -0.3880756
   0.6832714 ]
 [-0.26209524  1.3105342   1.5876237  ... -0.57300484 -1.1243302
   1.8980179 ]
 [ 0.5098745  -0.8308645   0.5639014  ...  0.4143082  -0.43875784
   0.00954971]]

wo ->>> [[ 1.0684972   0.88678735 -0.6828203  ...  1.6198356   1.4354376
   0.16771142]
 [-0.08717363  2.179152   -1.4764318  ... -0.46814412 -0.7814795
   0.31677097]
 [-0.34223688  0.5450925  -0.08186591 ...  0.83167946  1.1452315
   1.0985768 ]
 ...
 [ 0.76176184  1.295816   -0.7878585  ... -0.37668034 -1.4538118
  -1.0874062 ]
 [-0.07748459 -0.8757816   0.11903816 ...  0.8617923  -0.32771695
   1.186838  ]
 [ 0.4382756   0.7769573  -0.6754628  ... -0.09866794 -0.14121763
  -0.9270816 ]]
```