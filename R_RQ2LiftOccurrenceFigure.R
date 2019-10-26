library(ggplot2) 

ggplot(RQ2_Result, aes(x = reorder(Rules, order)))+
  geom_bar(aes(y = Values, fill=Type), position = "dodge", stat="identity") +
  ylab("Lift values")+
  # now adding the secondary axis
  #scale_y_continuous(sec.axis = sec_axis(~./1500, name = "Cumulative frequency"))+
  scale_y_continuous(sec.axis = sec_axis(~.-1), name = "Lift values")+
  coord_cartesian(ylim = c(1, 1.8)) +
  scale_fill_manual(values = c("#464159", "#8BBABB"))+
  labs(y = "Lift values",
       x = "",
       colour = "") +
  theme_light()+
  theme(panel.grid.minor.x = element_blank(),
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        axis.text.x = element_text(angle = 90, size = 13, hjust = 0.5,vjust = 0.5),
        axis.text.y = element_text(size = 13),
        axis.title.x = element_text(size = 13),
        axis.title.y = element_text(size = 13),
        legend.position="bottom",
        legend.title = element_blank(),
        
        legend.text = element_text(size = 13),
        legend.spacing.x = unit(0.5,"cm"),
        plot.margin = unit(c(0.3,0,0,0),"cm"))


