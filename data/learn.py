muscle_groups = [
    {
        "name": "Chest", 
        "url": "https://cdn.muscleandstrength.com/sites/default/files/taxonomy/image/videos/chest_0.jpg"
    },
    {
        "name": "Shoulders",
        "url": "https://cdn.muscleandstrength.com/sites/default/files/taxonomy/image/videos/shoulders_0.jpg"
    },
    {
        "name": "Back",
        "url": "https://cdn.muscleandstrength.com/sites/default/files/taxonomy/image/videos/upperback.jpg"
    },
    {
        "name": "Triceps", 
        "url": "https://cdn.muscleandstrength.com/sites/default/files/taxonomy/image/videos/triceps_0.jpg"
    },
    {
        "name": "Quads", 
        "url": "https://cdn.muscleandstrength.com/sites/default/files/taxonomy/image/videos/quads_1.jpg"
    },
    {
        "name": "Hamstrings",
        "url": "https://cdn.muscleandstrength.com/sites/default/files/taxonomy/image/videos/hamstrings_0.jpg"
    }
]

exercises = {
    "Chest": [
        {
            # https://www.muscleandstrength.com/exercises/barbell-bench-press.html
            "name": "Bench Press",
            "url": "https://www.youtube.com/embed/tuwHzzPdaGc",
            "primary": "Chest",
            "secondary": ["Shoulders", "Triceps"],
            "equipment": "Barbell",
            "description": "This is a staple chest exercise in nearly every workout program. For powerlifters, it is known as one of the big three which includes squat, deadlift, and bench press. For athletes, 1 rep max on bench press is a good indicator on performance. And for bodybuilders, it is a compound exercise that targets many muscles in the upper body.",
        },
        {
            # https://www.muscleandstrength.com/exercises/cable-crossovers-bent-over.html
            "name": "Cable Fly",
            "url": "https://www.youtube.com/embed/JHqmhZ12rr0",
            "primary": "Chest",
            "secondary": ["Shoulders", "Triceps"],
            "equipment": "Cable",
            "description": "This exercise is used to strengthen the pushing muscles of the body including the chest, triceps, and shoulders. It can be tough to overload as it requires a great deal of core stability, so it is probably best used as an accessory movement for those looking to increase their chest muscle mass.",
        },
        {
            # https://www.muscleandstrength.com/exercises/chest-dip.html
            "name": "Chest Dip",
            "url": "https://www.youtube.com/embed/FG1ENBFsdHU",
            "primary": "Chest",
            "secondary": ["Abs", "Shoulders", "Triceps"],
            "equipment": "Bodyweight",
            "description": "Chest dips effectively hit the lower region of the pec. It follows a vertical pressing movement pattern, which provides a unique stimulus for the muscles of the chest. It is best to master the bodyweight variation of this exercise prior to adding weight via weighted vests, belts, or chains.",
        },
    ],
    "Shoulders": [
        {
            # https://www.muscleandstrength.com/exercises/bent-over-cable-rear-delt-fly
            "name": "Rear Delt Fly",
            "url": "https://www.youtube.com/embed/Baavi8rJWBI",
            "primary": "Shoulders",
            "secondary": ["Traps"],
            "equipment": "Cable",
            "description": "The is an exercise used to target the muscles of the shoulder, specifically the rear deltoids. It can be performed during your shoulder workouts, upper body workouts, and full body workouts.",
        },
        {
            # https://www.muscleandstrength.com/exercises/dumbbell-upright-row.html
            "name": "Upright Row",
            "url": "https://www.youtube.com/embed/Cxrmdrq1s3E",
            "primary": "Shoulders",
            "secondary": ["Biceps", "Traps", "Upper Back"],
            "equipment": "Dumbbell",
            "description": "Upright rows are met with some controversy as many professionals view it as an exercise that promotes shoulder impingement. However, if performed appropriately it can be beneficial in targeting the shoulders to promote lean muscle growth.",
        },
        {
            # https://www.muscleandstrength.com/exercises/seated-shoulder-press.html
            "name": "Shoulder Press",
            "url": "https://www.youtube.com/embed/Gxhx7GpRb5g",
            "primary": "Shoulders",
            "secondary": ["Traps", "Triceps"],
            "equipment": "Barbell",
            "description": "This exercise is a variation of the overhead press and used to build shoulder strength and muscle. Vertical press variations are crucial movement patterns to train and should be incorporated into your workout routines.",
        },
    ],
    "Back": [
        {
            # https://www.muscleandstrength.com/exercises/tripod-dumbbell-row
            "name": "Tripod Row",
            "url": "https://www.youtube.com/embed/78Z2mk9LQoI",
            "primary": "Upper Back",
            "secondary": ["Abs", "Biceps", "Lats", "Lower Back", "Shoulders"],
            "equipment": "Dumbbell",
            "description": "This exercise requires more core stability than other more supported row variations. It also allows one to work the muscles of the back unilaterally, which can lead to a more symmetrical physique and balanced strength.",
        },
        {
            # https://www.muscleandstrength.com/exercises/machine-t-bar-row.html
            "name": "T-Bar Row",
            "url": "https://www.youtube.com/embed/kHW23afzaUs",
            "primary": "Upper Back",
            "secondary": ["Biceps", "Lats", "Shoulders"],
            "equipment": "Machine",
            "description": "The back is a muscle group that requires a fair amount of variation. So, experiment with several different angles and hand positions to maximize your back muscle growth.",
        },
        {
            # https://www.muscleandstrength.com/exercises/bent-over-barbell-row.html
            "name": "Bent Over Row",
            "url": "https://www.youtube.com/embed/paCfxhgW6bI",
            "primary": "Upper Back",
            "secondary": ["Abs", "Biceps", "Lats", "Lower Back", "Shoulders"],
            "equipment": "Barbell",
            "description": "Those in powerlifting and strength circles perform bent over rows to increase their strength on the big three movements. This exercise is typically used to build and strengthen the muscles of the upper back. However, it requires assistance from muscles of the lower back, core, and arms to perform correctly.",
        },
    ],
    "Triceps": [
        {
            # https://www.muscleandstrength.com/exercises/rope-tricep-extension.html
            "name": "Tricep Extension",
            "url": "https://www.youtube.com/embed/LzwgB15UdO8",
            "primary": "Triceps",
            "secondary": [],
            "equipment": "Cable",
            "description": "Well-built triceps have a lot of positive carryover into your pressing movements such as bench press variations and shoulder press variations. The exercise can be included in your tricep workouts, upper body workouts, push workouts, and full body workouts.",
        },
        {
            # https://www.muscleandstrength.com/exercises/ez-bar-skullcrusher.html
            "name": "Skullcrusher",
            "url": "https://www.youtube.com/embed/K6MSN4hCDM4",
            "primary": "Triceps",
            "secondary": [],
            "equipment": "EZ Bar",
            "description": "The triceps can be trained in many different ways to promote growth. The EZ bar skullcrusher is an effective way to target the long head of the tricep. Having bigger and stronger triceps are not only important from an aesthetic standpoint but can also help contribute to better performance on pressing motions.",
        },
        {
            # https://www.muscleandstrength.com/exercises/bent-over-dumbbell-kickback.html
            "name": "Tricep Kickback",
            "url": "https://www.youtube.com/embed/BL9CzOQZDrs",
            "primary": "Triceps",
            "secondary": [],
            "equipment": "Dumbbell",
            "description": "This is a classic tricep exercise that has been used for ages. The movement should be slow and focused, and the point of this exercise is to get a good contraction on the triceps and establish a mind-muscle connection.",
        },
    ],
    "Hamstrings": [
        {
            # https://www.muscleandstrength.com/exercises/stiff-leg-deadlift-aka-romanian-deadlift.html
            "name": "Stiff Leg Deadlift",
            "url": "https://www.youtube.com/embed/CkrqLaDGvOA",
            "primary": "Hamstrings",
            "secondary": ["Abs", "Adductors", "Calves", "Glutes", "Lats", "Lower Back", "Quads", "Traps", "Upper Back"],
            "equipment": "Barbell",
            "description": "The stiff leg deadlift has long been thought of as the leg deadlift variation, despite all hip hinge movements primarily targeting the hamstrings. It is best utilized during your leg workouts or full body workouts.",
        },
        {
            # https://www.muscleandstrength.com/exercises/seated-leg-curl
            "name": "Leg Curl",
            "url": "https://www.youtube.com/embed/3BWiLFc8Dbg",
            "primary": "Hamstrings",
            "secondary": ["Glutes"],
            "equipment": "Machine",
            "description": "The seated leg curl is a variation of the leg curl and an exercise used to isolate the hamstrings. This exercise is best used as part of your leg workout or in a full body workout routine.",
        },
        {
            # https://www.muscleandstrength.com/exercises/nordic-hamstring-curl-bodyweight
            "name": "Nordic Hamstring Curl",
            "url": "https://www.youtube.com/embed/rzK7glg8OnA",
            "primary": "Hamstrings",
            "secondary": ["Abs", "Calves", "Glutes"],
            "equipment": "Machine",
            "description": "Nordic hamstring curls are very challenging. However, they do an excellent job at building hamstring muscle and strength which will have a positive carry over into your leg exercises and aesthetics.",
        },
    ],
    "Quads": [
        {
            # https://www.muscleandstrength.com/exercises/squat.html
            "name": "Squat",
            "url": "https://www.youtube.com/embed/R2dMsNhN3DE",
            "primary": "Quads",
            "secondary": ["Calves", "Glutes", "Hamstrings", "Lower Back"],
            "equipment": "Barbell",
            "description": "This exercise is known as one of the big three which includes squat, deadlift, and bench press. It is a compound exercise that targets nearly every muscle of your lower body and core. Over the years, several squatting variations have been developed to help everyone be able to train this critical movement pattern safely.",
        },
        {
            # https://www.muscleandstrength.com/exercises/45-degree-leg-press.html
            "name": "Leg Press",
            "url": "https://www.youtube.com/embed/sEM_zo9w2ss",
            "primary": "Quads",
            "secondary": ["Abs", "Adductors", "Calves", "Glutes", "Hamstrings", "Lower Back"],
            "equipment": "Machine",
            "description": "One can utilize the leg press to target both the quads and the hamstring muscle, depending on which portion of the foot they push through. The leg press is best used as an accessory movement to the squat, or as a primary movement in gyms which lack the necessary equipment to train the squat movement pattern.",
        },
        {
            # https://www.muscleandstrength.com/exercises/leg-extension.html
            "name": "Leg Extension",
            "url": "https://www.youtube.com/embed/0fl1RRgJ83I",
            "primary": "Quads",
            "secondary": [],
            "equipment": "Machine",
            "description": "The leg extension is a great exercise for quad development. However, for those with prior knee issues, it may be beneficial to stick with other movements to target your quads.",
        },
    ],
}
