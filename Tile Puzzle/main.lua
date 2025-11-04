local love =  require("love")
local button = require("button")
local screen = {
    height = love.graphics.getHeight(),
    width = love.graphics.getWidth(),
}
local win_color = {red = 0, green = 0, blue = 0, red_increase = true, green_increase = false, blue_increase = false, spin=0}
local player_cursor = {
    x = 0,
    y = 0,
}
local buttons = {}
local state = {
    playing = true,
    stage = 1,
    win = false
}
local max_grid = {
    x = 0,
    y = 0
}


function love.load()
    love.window.setTitle("Tile Puzzle")
    love.mouse.setVisible(false)
    for x = 1, 5 do
        max_grid.x = x
        for y = 1, 3 do
            table.insert(buttons, 1, Button((((screen.width/2)+48) - ((x-1)*32)), (((screen.height/2)+16) - ((y-1)*32)), x, y))
            max_grid.y = y
        end
    end
end

function love.update()
    player_cursor.x, player_cursor.y = love.mouse.getPosition()
    if state.playing == true then
        for i = 1, #buttons do
            local pressed = buttons[i]:pressed(player_cursor.x, player_cursor.y)
            if pressed then
                if i+1 < max_grid.x * max_grid.y+1 and i % max_grid.y ~= 0 then
                    buttons[i+1]:force_press()
                end
                if i-1 > 0 and (i-1) % max_grid.y ~= 0 then
                    buttons[i-1]:force_press()
                end
                if i+max_grid.y < max_grid.x * max_grid.y+1 then
                    buttons[i+max_grid.y]:force_press()
                end
                if i-max_grid.y > 0 then
                    buttons[i-max_grid.y]:force_press()
                end
            end
        end
        
        local button_checks = 0
        for i = 1, #buttons do
            if buttons[i].press_check == true then
                button_checks = button_checks + 1
            end
        end
        if button_checks == max_grid.x * max_grid.y then
            state.playing = false
        else
            button_checks = 0
        end
    else
        if state.stage > 3 then
            state.win = true
        else
            if not state.win then
                state.stage = state.stage + 1
                buttons = {}
                if state.stage == 2 then
                    for x = 1, 5 do
                        max_grid.x = x
                            for y = 1, 5 do
                                table.insert(buttons, 1, Button((((screen.width/2)+48) - ((x-1)*32)), (((screen.height/2)+48) - ((y-1)*32)), x, y))
                                max_grid.y = y
                            end
                    end
                else
                    for x = 1, 8 do
                        max_grid.x = x
                            for y = 1, 5 do
                                table.insert(buttons, 1, Button((((screen.width/2)+96) - ((x-1)*32)), (((screen.height/2)+48) - ((y-1)*32)), x, y))
                                max_grid.y = y
                            end
                    end
                end
                state.playing = true
            end
        end
    end
end

function love.draw()
    if state.playing == true then
        for i = 1, #buttons do
            buttons[i]:draw()
        end
    end
    if state.win then
        if win_color.red >= 1 then
            win_color.red_increase = false
            win_color.green_increase = true
        end
        if win_color.green >= 1 then
            win_color.green_increase = false
            win_color.blue_increase = true
        end
        if win_color.blue >= 1 then
            win_color.blue_increase = false
            win_color.red_increase = true
        end
        if win_color.red_increase then
            win_color.red = win_color.red + 0.02
            if win_color.green > 0 then
                win_color.green = win_color.green - 0.02
            end
            if win_color.blue > 0 then
                win_color.blue = win_color.blue - 0.02
            end
        end
        if win_color.green_increase then
            win_color.green = win_color.green + 0.02
            if win_color.red > 0 then
                win_color.red = win_color.red - 0.02
            end
            if win_color.blue > 0 then
                win_color.blue = win_color.blue - 0.02
            end
        end
        if win_color.blue_increase then
            win_color.blue = win_color.blue + 0.02
            if win_color.green > 0 then
                win_color.green = win_color.green - 0.02
            end
            if win_color.red > 0 then
                win_color.red = win_color.red - 0.02
            end
        end
        if win_color.red < 0 then
            win_color.red = 0
        end
        if win_color.green < 0 then
            win_color.green = 0
        end
        if win_color.blue < 0 then
            win_color.blue = 0
        end
        win_color.spin = win_color.spin + 0.025
        if win_color.spin > 360 then
            win_color.spin = 0
        end
        love.graphics.setColor(win_color.red, win_color.green, win_color.blue, 1)
        love.graphics.print("your're did it", (screen.width/2), (screen.height/2), win_color.spin, 5, 5, 37.5, 10)
        love.graphics.print(win_color.red, 5, 50)
        love.graphics.print(win_color.green, 5, 75)
        love.graphics.print(win_color.blue, 5, 100)
    end
    love.graphics.print(state.stage .. "/3", 30, 30)
    love.graphics.circle("fill", player_cursor.x-1, player_cursor.y+-1, 5)
end