# The Endless Browser
The Endless Browser is a secure IPFS browser prototype.

It isolates the IPFS in a container (docker) which has limited isolation with your environment.This allows for a better web.

### Current Phase

Design

### Basic Design

There is an endless server running on the host OS. There is also a docker image running in a container on the host os. The container provides an isolated environment, while the endless server serves to manage an explicit protocol between the host environment and the isolated environment.

The endless server manages information contained in 2 folders on the host OS and delivers that information to requests from the endless process running inside the container. The two folders it essentially manages is: Identity and Private.

The docker container mounts 3 folders: Public, Cache, Pin. When content is downloaded from the IPFS network it is placed in Cache, if it is pinned permanently it is placed in Pin. Public is a folder designated for providing your own public files to the network, though all three folders' contents are available to the IPFS network. The public folder can be thought of as the folder you might put things if you want to host a site.

HOST OS:
 - endless server (manages...)
   - Idenitity namespace
   - Private namespace
 - endless container (mounts...)
   - Public namespace (permanent home for internally managed mutating systems ("sites"))
   - Cache namespace (temporary home for externally managed mutating systems)
   - Pin namespace (permanent home for externally managed mutating systems)

### Benefits

Code is just data; data that describes changes in data. With this design you can write code in any language that the isolated environment knows and thereby build systems much more dynamic and flexible than current webdesigned archetecture will eaily allow day. By isolating the environment where the distributed code is ran, we eliminate much of the burden placed on todays webbrowser and thereby anniahilate limitation imposed upon distributed systems by the bottleneck of the webbrowser.
