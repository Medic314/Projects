local love =  require("love")

function Dice(x, y)
    return {
        x = x,
        y = y,

        sprite = {
            image = love.graphics.newImage("image/dice_sprites.png"),
            sprite_width = 192,
            sprite_height = 32,
            quad_width = 32,
            quad_height = 32,

            quads = {
                love.graphics.newQuad(32 * 0, 0, 32, 32, 192, 32),
                love.graphics.newQuad(32 * 1, 0, 32, 32, 192, 32),
                love.graphics.newQuad(32 * 2, 0, 32, 32, 192, 32),
                love.graphics.newQuad(32 * 3, 0, 32, 32, 192, 32),
                love.graphics.newQuad(32 * 4, 0, 32, 32, 192, 32),
                love.graphics.newQuad(32 * 5, 0, 32, 32, 192, 32)
            }
        },

        dice_load = function(self)
            love.graphics.draw(self.sprite.image, self.sprite.quads[1], self.x, self.y)
        end
    }

end


return Dice()