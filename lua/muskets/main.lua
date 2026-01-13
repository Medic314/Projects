local love = require("love")
require("dice")
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
end


function love.update()
    cursor.x, cursor.y = love.mouse.getPosition()
    dice_interact(5,5,cursor.x,cursor.y)
end


function love.draw()
    dice_draw(5, 5)
end