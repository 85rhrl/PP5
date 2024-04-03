import { rest } from "msw";

const baseURL = "https://pp5-85rhrl-766ed649dea1.herokuapp.com/";

export const handlers = [
  rest.get(`${baseURL}dj-rest-auth/user/`, (req, res, ctx) => {
    return res(
      ctx.json({
        pk: 4,
        username: "bishop",
        email: "",
        first_name: "",
        last_name: "",
        profile_id: 4,
        profile_image:
          "https://res.cloudinary.com/dgpqn0ewc/image/upload/v1/media/images/Bishop-Aliens-Lance-Heriksen-Synthetic_trzv1d",
      })
    );
  }),
  rest.post(`${baseURL}dj-rest-auth/logout/`, (req, res, ctx) => {
    return res(ctx.status(200));
  }),
];
