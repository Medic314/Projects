_G.love = require("love")

function love.load()
    _G.character = {
        x = 0,
        y = 50,
        sprite = love.graphics.newImage("image/rainbow.png"),
        animation = {
            direction = "right",
            idle = true,
            frame = 1,
            max_frames = 6,
            speed = 30,
            timer = 0.1}}
    -- 566x91 
    SPRITE_WIDTH, SPRITE_HEIGHT = 600, 100
    QUAD_WIDTH = 100
    QUAD_HEIGHT = SPRITE_HEIGHT

    quads = {}

    for i= 1, 6 do
        quads[i] = love.graphics.newQuad(QUAD_WIDTH * (i-1), 0, QUAD_WIDTH, QUAD_HEIGHT, SPRITE_WIDTH, SPRITE_HEIGHT)
    end
end

function love.update(dt)
    if love.keyboard.isDown("d") then
        character.animation.idle = false
        character.animation.direction = "right"
    elseif love.keyboard.isDown("a") then
        character.animation.idle = false
        character.animation.direction = "left"
    else
        character.animation.idle = true
        character.animation.frame = 1
    end
    if not character.animation.idle then
        character.animation.timer = character.animation.timer + dt
    end
    if character.animation.timer > 0.2 then
        character.animation.timer = 0.1
        
        character.animation.frame = character.animation.frame + 1
   
        if character.animation.direction == "right" then
            character.x = character.x + character.animation.speed
        elseif character.animation.direction == "left" then
            character.x = character.x - character.animation.speed
        end

        if character.animation.frame > character.animation.max_frames then
            character.animation.frame = 1
        end

    end
end

function love.draw()
    love.graphics.draw(character.sprite, quads[character.animation.frame], character.x, character.y)
end