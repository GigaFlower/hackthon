/**
 * Created by BigFlower on 16/11/27.
 */
'use strict';

var emotion_speed = {
    anger: 10,
    disgust: 8,
    fear: 3,
    joy: 6,
    sadness: 1,
    analytical: 4,
    tentative: 7
};

function add_audio_by_emotion(emotion_obj){
    // emotion_obj is something like { <emotion_name>:<weight_float_between_0_1> ... }
    var spd = emotion_values_to_speed(emotion_obj);
    var fname = get_audio_name_by_speed(spd);
    add_audio(fname);
}

function emotion_values_to_speed(emotion_obj) {
    var speed = 0.0, weights = 0.0;
    for (var emo in emotion_obj) {
        speed += emotion_speed[emo] * emotion_obj[emo];
        weights += emotion_speed[emo];
    }
    speed /= weights;
    return speed;
}


function get_audio_name_by_speed(speed) {
    var level = '';
    if (speed < 0 || speed > 10) {
        return '';
    } else if (speed <= 2) {
        level = 'slower';
    } else if (speed <= 4) {
        level = 'slow';
    } else if (speed <= 6) {
        level = 'normal';
    } else if (speed <= 8) {
        level = 'fast';
    } else {
        level = 'faster';
    }

    var ind = Math.floor(Math.random() * 10);
    return level + '00' + ind + 'mp3';
}

function add_audio(file_name){
    var audio = document.createElement("audio");
    audio.setAttribute("src","/static/music/" + file_name);
    audio.setAttribute("loop","false");
    audio.setAttribute("autoplay", "autoplay");
    audio.setAttribute("hidden", "hidden");
    document.appendChild(audio);
}