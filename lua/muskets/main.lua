local love =  require("love")
local dice = require("dice")
local screen = {
    height = love.graphics.getHeight(),
    width = love.graphics.getWidth(),
}

local game = {
    state = {
        main_menu = false,
        paused = false,
        shop = false,
        running = true
    }
}

local player_info = {
    items = {}
}

local cursor = {
    x = 0,
    y = 0
}






function love.load()
    love.window.setTitle("--= MUSKETS =--")
    Dice(50, 50)
end


function love.update()

end


function love.draw()

end