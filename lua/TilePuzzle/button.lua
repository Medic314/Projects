local love =  require("love")

function Button(x, y, grid_x, grid_y)
    return {
        sprites = {sprite_neutral = love.graphics.newImage("image/black.png"),
        sprite_pressed = love.graphics.newImage("image/white.png")},
        x = x,
        y = y,
        press_check = false,
        mouse_pressed = false,
        force_press = function(self)
            if self.press_check then
                self.press_check = false
            else
                self.press_check = true
            end
        end,
        pressed = function(self, player_cursor_x, player_cursor_y)
            if player_cursor_x < self.x + 32 and player_cursor_x > self.x and player_cursor_y < self.y + 32 and player_cursor_y > self.y then
                if love.mouse.isDown(1) then
                    if self.mouse_pressed == false then
                        if not self.press_check then
                            self.press_check = true
                            self.mouse_pressed = true
                            return true
                        else
                            self.press_check = false
                            self.mouse_pressed = true
                            return true
                        end
                    end
                end
                if not love.mouse.isDown(1) then
                    self.mouse_pressed = false
                end
            else
                return false
            end
        end,
        draw = function(self)
            if self.press_check == false then
                love.graphics.draw(self.sprites.sprite_neutral, self.x, self.y)
            else
                love.graphics.draw(self.sprites.sprite_pressed, self.x, self.y)
            end
        end}
end
return Button()