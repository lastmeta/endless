# The Endless Browser

IPFS + Docker [+ Browser]

### Goal

A better, more distributed web.

### Current Phase

Design

### Basic Design

![Highest Level Diagram](/assets/images/basic_design.png)

There is an endless server running on the host OS. There is also a docker image running in a container on the host os. The container provides an isolated environment, while the endless server serves to manage an explicit protocol between the host environment and the isolated environment.

The endless server manages information contained in 2 folders on the host OS and delivers that information to requests from the endless process running inside the container. The two folders it essentially manages is: Identity and Private.

The docker container mounts 3 folders: Public, Cache, Pin. When content is downloaded from the IPFS network it is placed in Cache, if it is pinned permanently it is placed in Pin. Public is a folder designated for providing your own public files to the network, though all three folders' contents are available to the IPFS network. The public folder can be thought of as the folder you might put things if you want to host a site-app.

HOST OS:
 - endless server (manages...)
   - Identity namespace
   - Private namespace
 - endless container (mounts...)
   - Public namespace (permanent home for internally managed mutating systems ("site-apps"))
   - Cache namespace (temporary home for externally managed mutating systems)
   - Pin namespace (permanent home for externally managed mutating systems)

### Vision

Imagine, (merely because we tend to stick with known paradigms) that you wanted to create a website on this system: one that would authenticate the user, save preferences and details and perform some kind of logic to deliver information to the client.

The website would be saved to the client's machine (into the docker image of course, specifically the cache mounted folder). That is the front end UI, the backend logic and any static data that this user should always have access to. The code runs locally in the container and is, ideally, open source.

Everything one system saves can be captured by nefarious code in another system therefor everything is meant to be encrypted and unlocked by keys retrieved in the Identities namespace (which is only accessible through a very particular protocol with the endless server). In this manner client or user data is always kept on the user machine, code or system logic is also kept on the user's system and the only thing you may need to talk to an external server for is authentication and direct information transfer.

### Benefits

Code is just data; data that describes changes in data. With this design you can write code in any language that the isolated environment knows and thereby build systems much more dynamic and flexible than current web designed architecture will easily allow day. By isolating the environment where the distributed code is ran, we eliminate much of the burden placed on todays web browser and thereby annihilate limitation imposed upon distributed systems by the bottleneck of the web browser.

As distributed computing becomes more ubiquitous, this design allows much more flexibility as it is essentially language agnostic.
