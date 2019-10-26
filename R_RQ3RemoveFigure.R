ggplot() +
  geom_linerange(data = RQ3LikertRemove, 
                 aes(x = reorder(CoCodes, Order), 
                     #aes(x = CoCodes,
                     ymin = StartPercent, 
                     ymax = EndPercent,
                     color = as.factor(Standard)),
                 size = 8)+
  guides(color = guide_legend(override.aes = list(size = 6),keyheight =1,title = NULL))+
  
  
  scale_color_manual(breaks = 7:1,
                     labels = rev(c("","","","within one week",
                                    "more than one week, less than one month","more than one month, less than one year", "more than one year" )), 
                     
                  
                     values = c("#C7F0DB","#8BBABB","#6C7B95","#464159","#6C7B95","#8BBABB","#C7F0DB")
  )+
  
  
  geom_hline(aes(yintercept = 0),alpha = 0.2,size = 0.5)+
  scale_y_continuous(name = NULL, limits = c(-1.0,1.0),labels = scales::percent)+
  scale_x_discrete(name = "rule(a,b)")+
  
  theme_light()+
  theme(panel.grid.minor.x = element_blank(),
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        axis.text.x = element_text(angle = 90, size = 11, hjust = 1,vjust = 0.5),
        axis.text.y = element_text(size = 11),
        axis.title.x = element_text(size = 13),
        legend.position = "bottom",
        legend.text = element_text(size = 13),
        legend.spacing.x = unit(0.7, 'cm'))
       

