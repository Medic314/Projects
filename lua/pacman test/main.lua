_G.love = require("love")

function love.load()
    love.graphics.setBackgroundColor(0.5, 0.5, 1)

    _G.pacman = {}
    pacman.x = 200
    pacman.y = 250
    pacman.angle1 = 1
    pacman.angle2 = 5
    pacman.speed = 1

    _G.food = {
        x = 600,
        eaten = false
    }
end

function love.update(dt)
   if pacman.x >= food.x + 20 then
    food.eaten = true
   end
   if love.keyboard.isDown("down") then
    pacman.angle1 = pacman.angle1 - 0.5
    pacman.angle2 = pacman.angle2 - 0.5
   end
   if love.keyboard.isDown("lshift") then
    pacman.speed = 10
   else
    pacman.speed = 3.5
   end
   if love.keyboard.isDown("a") then
    pacman.x = pacman.x - pacman.speed
   end
   if love.keyboard.isDown("w") then
    pacman.y = pacman.y - pacman.speed
   end
   if love.keyboard.isDown("s") then
    pacman.y = pacman.y + pacman.speed
   end
   if love.keyboard.isDown("d") then
    pacman.x = pacman.x + pacman.speed
   end
end

function love.draw()
    if not food.eaten then
        love.graphics.setColor(0, 0, 0)
        love.graphics.rectangle("fill", food.x, 200, 70, 70)
    end

    love.graphics.setColor(1, 0.7, 0.1)
    love.graphics.arc("fill", pacman.x, pacman.y, 60, pacman.angle1, pacman.angle2)
    love.graphics.print(pacman.speed)
end