local love =  require("love")

dice_info = {
    sprite = {
        image = love.graphics.newImage("image/dice_sprites.png"),
        quads = {}
    },
    
}

for i= 1, 6 do
    dice_info.sprite.quads[i] = love.graphics.newQuad(32 * (i-1), 0, 32, 32, 192, 32)
end

dice_interact = function(x, y, cursor_x, cursor_y)
    if love.mouse.isDown(1) then
        if cursor_x < x+32 and cursor_x > x-32 and cursor_y < y+32 and cursor_y > y-32  then
            print("pressed")
        end
    end
end

dice_draw = function(x,y)
    love.graphics.draw(dice_info.sprite.image, dice_info.sprite.quads[1], x, y)
end