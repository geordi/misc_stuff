
## Allow more watched files

[Github Issue](https://github.com/gatsbyjs/gatsby/issues/11406)

`echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p`
