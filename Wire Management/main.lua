local love =  require("love")

local player_cursor = {
    x = 0,
    y = 0,
}

local button = {
    sprite_neutral = love.graphics.newImage("image/button.png"),
    sprite_pressed = love.graphics.newImage("image/button_pressed.png"),
    x = 150,
    y = 150,
    sprite_current = love.graphics.newImage("image/button.png")
}

function love.load()
    love.window.setTitle("Wire Management")
    love.mouse.setVisible(false)
end

function love.update()
    player_cursor.x, player_cursor.y = love.mouse.getPosition()
    if love.mouse.isDown(1) then
        if player_cursor.x < button.x + 32 and player_cursor.x > button.x and player_cursor.y < button.y + 32 and player_cursor.y > button.y then
            button.sprite_current = button.sprite_pressed
        end
    else
        button.sprite_current = button.sprite_neutral
    end
end

function love.draw()
    love.graphics.draw(button.sprite_current, button.x, button.y)
    love.graphics.circle("fill", player_cursor.x-1, player_cursor.y+-1, 5)
end