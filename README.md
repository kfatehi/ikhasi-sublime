# What?
get sublime to print your current sublime text content view into an html div over websockets

# How?
0. clone and cd into repo
1. `ln -s $PWD/sublime_package ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/ikhasi-sublime.sublime_package`
2. Start the server `cd server`, `npm install`, `node server.js`
3. Lift sails (XD) `cd html_client`, `npm install`, `sails lift`

For a much more baked implementation, check out [Floobits](http://floobits.com)