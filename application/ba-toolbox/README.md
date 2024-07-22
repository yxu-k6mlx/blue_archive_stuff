## ba-toolbox / BA工具盒
This project is aimed at providing a web-based alternative to the existing popular Blue Archive fan-made story editor/viewer AzureArchive. The plan is as follows. 

本项目纯属等AzureArchive修bug等的无聊了写的东西，计划是写一个网页就能用的AA开源自研翻版。

## Planning / 工程计划
Keep in mind I literally just made this repo not that long ago, so everything below is subject to change. 

以下是目前为止的一些工程实现设想，鉴于这个工程刚刚开始，以下内容随时可能变动。

### Frameworks / 框架
This project is planned to be a broswer based application. The server-side rendering will be done mostly in `Node.js`, while the client-size rendered front-end will be built on `React.js`. 

本项目计划使用`React.js`支援客户端UI渲染搭配`Node.js`支援后端渲染。

Again, this is (so far) planned to be a `React.js` project as an opportunity for me to learn React. No idea how this will work out cuz I have very minimal experiences in this field. Let's see how this goes. 

鉴于本人对`React.js`和`Node.js`一无所知所以这个项目也是逼我自己学前端的一个项目，前程依旧充满未知。

### Story Scripting / 故事编辑系统
The stories themselves are planned to be represented by ".archive" files which are json files with a different subfix to avoid confusion. 

目前的计划是使用".archive"后缀json文件作为剧情描述工具。

### Hosting & Serving Codes / 后端相关
No idea. Right now it's running on magic by Vercel. I've no idea what they use besides that they use `Node.js`. I might change it to `Django` + `Node.js` if I do get my own server for this. 

优质回答：我不知道。Vercel提供了一个（目前还）可以免费host网站的服务，具体细节和未来我也不知道。

## About / 关于
### Who are you? / 你是谁? 
I'm K6MLX. Yes that's a FCC HAM callsign. You can find me on air if you live around California and tune in to CARLA radio system. For more information, please refer to my github.io page at yxu-k6mlx.github.io. 

### Why am I doing this? / 为什么开发这个项目? 
I can't find a job without a proper portfolio, and when I wanted to write some fan-fic for Blue Archive, AzureArchive broke on me. And since that app is built with Unity with no publicly available source code, I can't even help fix it. So I said fuck it and am building an open-source alternative to AA and use this oppotunity to hopefully build a good enough portfolio so someone will hire me lol. 

毕业已足一月之久，然求职无果，遂开发项目。万一开发出来了呢？
### Who can contribute? / 谁可以贡献? 
If you are interested, please contact me first using all my contacts listed on [my website](https://yxu-k6mlx.github.io/Contact/contact.html), then I will give you my Discord contact. Then we'll go from here. 

汝若有致，还请移步[联络信息站](https://yxu-k6mlx.github.io/Contact/contact.html)。

### What's the plan? / 计划为何? 
Please refer to the illustrations below. 
![General Planning](./public/plans/general_planning.png?raw=true)
![Dialog Screen Planning](./public/plans/dialog_planning.png?raw=true)


## Additional Information / 更多信息
This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

The main branch of this project is deployed directly to [blue-archive-stuff](https://blue-archive-stuff.vercel.app/), hosted by Vercel. 
